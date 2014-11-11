import os
import re
import inspect
from copy import copy
from contextlib import contextmanager
from sugarbowl import merge_dicts
from ..helpers import Null, join
from ..settings import settings
from .metaclass import Metaclass
from .module import Module
from .require import require
from .event import CallTaskEvent
from .trigger import trigger


class Task(metaclass=Metaclass):

    # Public

    def __init__(self, *args, **kwargs):
        self.__args = args
        self.__kwargs = kwargs

    def __get__(self, module, module_class=None):
        return self

    def __getattribute__(self, name):
        try:
            return super().__getattribute__(name)
        except AttributeError:
            if self.__check_inheritance(name):
                if self.meta_module is not None:
                    try:
                        return getattr(self.meta_module, name)
                    except AttributeError:
                        pass
        raise AttributeError(
            'Task "{self}" has no attribute "{name}".'.
            format(self=self, name=name))

    def __call__(self, *args, **kwargs):
        Event = CallTaskEvent
        args = self.meta_args + args
        kwargs = merge_dicts(self.meta_kwargs, kwargs)
        self.meta_notify(Event(self, Event.INIT, *args, **kwargs))
        try:
            self.__resolve_dependencies()
            try:
                with self.__change_directory():
                    result = self.meta_invoke(*args, **kwargs)
            except Exception:
                if self.meta_fallback is not None:
                    result = self.meta_fallback
                else:
                    self.__resolve_dependencies(fail=True)
                    raise
            self.__resolve_dependencies(fail=False)
        except Exception:
            self.meta_notify(Event(self, Event.FAIL, *args, **kwargs))
            raise
        self.meta_notify(Event(self, Event.DONE, *args, **kwargs))
        return result

    def __repr__(self):
        template = '<{self.meta_type}>'
        if self.meta_qualname:
            template = '<{self.meta_type} "{self.meta_qualname}">'
        return template.format(self=self)

    @property
    def meta_args(self):
        """Tasks's default arguments
        """
        return self.__args

    @property
    def meta_basedir(self):
        """Task's basedir.

        If meta_chdir is True current directory will be
        changed to meta_basedir when task invoking.
        """
        return self.meta_inspect(
            name='basedir', lookup=True, default=None)

    @property
    def meta_chdir(self):
        """Task's chdir status (enabled or disabled).

        .. seealso:: :attr:`run.Task.meta_basedir`
        """
        return self.meta_inspect(
            name='chdir', lookup=True, inherit=True,
            default=settings.chdir)

    @classmethod
    def meta_create(cls, *args, **kwargs):
        # Create task object
        self = object.__new__(cls)
        # Initiate parameters
        self.__parameters = {}
        for key in list(kwargs):
            if key.startswith('meta_'):
                name = key.replace('meta_', '')
                self.__parameters[name] = kwargs.pop(key)
        # Initiate dependencies
        self.__dependencies = []
        self.__init_dependencies()
        # Initiate directories
        self.__localdir = os.path.abspath(os.getcwd())
        # Initiate cache
        self.__cached_result = Null
        # Initiate arguments
        self.__args = ()
        self.__kwargs = {}
        # Call user init
        self.__init__(*args, **kwargs)
        return self

    def meta_depend(self, dependency):
        """Add custom dependency.

        Parameters
        ----------
        dependency: :class:`.dependency.Dependency`
            Dependency to be dependent upon.
        """
        dependency.bind(self)
        self.meta_dependencies.append(dependency)

    @property
    def meta_dependencies(self):
        """Task's list of dependencies.
        """
        return self.__dependencies

    @property
    def meta_docstring(self):
        """Task's docstring.
        """
        return self.meta_inspect(
            name='docstring', lookup=True,
            default=str(inspect.getdoc(self)).strip())

    @property
    def meta_fallback(self):
        """Task's fallback.

        Fallback used when task invocation fails.
        """
        return self.meta_inspect(
            name='fallback', lookup=True, inherit=True,
            default=settings.fallback)

    @property
    def meta_inherit(self):
        return self.meta_inspect(
            name='inherit', lookup=True, default=['meta_*'])

    def meta_inspect(self, name, *, lookup=False, inherit=False, default=None):
        """Return internal meta parameter.

        Parameters
        ----------
        name: str
            Name of parameter.
        lookup: bool
            Allow to lookup from init parameters.
        inherit: bool
            Allow to inherit from meta_module.
        default: mixed
            Default value.

        Returns
        -------
        mixed
            Value of parameter.
        """
        fullname = 'meta_' + name
        if lookup:
            if name in self.__parameters:
                return self.__parameters[name]
        if inherit:
            inherit = self.__check_inheritance(fullname)
        if inherit:
            if self.meta_module is not None:
                try:
                    return getattr(self.meta_module, fullname)
                except AttributeError:
                    pass
        return default

    def meta_invoke(self, *args, **kwargs):
        """Invoke task.

        Parameters
        ----------
        args, kwargs
            Arguments for task invokation.
        """
        pass

    @property
    def meta_is_descriptor(self):
        return False

    @property
    def meta_kwargs(self):
        """Tasks's default keyword arguments.
        """
        return self.__kwargs

    @property
    def meta_listeners(self):
        return self.meta_inspect(
            name='listeners', lookup=True, default=[])

    @property
    def meta_main_module(self):
        """Task's main module of module hierarchy.
        """
        main_module = None
        if self.meta_module:
            main_module = self.meta_module.meta_main_module
        return main_module

    @property
    def meta_module(self):
        """Task's module.
        """
        return self.meta_inspect(
            name='module', lookup=True, default=None)

    @property
    def meta_name(self):
        """Task's name.

        Name is defined as task name in module.
        """
        name = ''
        if self.meta_module:
            tasks = self.meta_module.meta_tasks
            for key, task in tasks.items():
                if task is self:
                    name = key
        return name

    def meta_not_depend(self, task):
        """Remove all of task dependencies.

        Parameters
        ----------
        task: str
            Task name to be not dependent upon.
        """
        task = self.meta_module.meta_lookup(task)
        for dependency in copy(self.meta_dependencies):
            if dependency.predecessor is task:
                self.meta_dependencies.remove(dependency)

    # TODO: add event flow management (like stop propognation)
    def meta_notify(self, event):
        for listener in self.meta_listeners:
            listener(event)
        if self.meta_module:
            self.meta_module.meta_notify(event)

    @property
    def meta_qualname(self):
        qualname = ''
        if self.meta_module:
            qualname = '.'.join(filter(None,
                [self.meta_module.meta_qualname,
                 self.meta_name]))
        return qualname

    # TODO: rename to make_path?
    def meta_path(self, *components, local=False):
        basedir = self.meta_basedir
        if basedir is None or not os.path.isabs(basedir):
            prefix = self.__localdir
            if self.meta_module:
                prefix = self.meta_module.meta_path(local=local)
            basedir = join(prefix, self.meta_basedir)
        path = join(basedir, *components)
        return path

    def meta_require(self, task, *args, **kwargs):
        """Add require dependency.

        Parameters
        ----------
        task: str
            Task name to require.
        args, kwargs
            Arguments for dependency resolve call.
        """
        dependency = require(task, *args, **kwargs)
        self.meta_depend(dependency)

    def meta_retrieve(self, name, *, module=False, default=None):
        """Return meta parameter
        """
        if name in self.__parameters:
            return self.__parameters[name]
        if not isinstance(self, Module):
            if self.meta_module:
                return self.meta_module.meta_retrieve(name, default=default)
        return default

    @property
    def meta_signature(self):
        """Task's signature.
        """
        return self.meta_inspect(
            name='signature', lookup=True,
            default=str(inspect.signature(self.meta_invoke)))

    @property
    def meta_style(self):
        return self.meta_inspect(
            name='style', lookup=True, default='task')

    def meta_trigger(self, task, *args, **kwargs):
        """Add trigger dependency.

        Parameters
        ----------
        task: str
            Task name to trigger.
        args, kwargs
            Arguments for dependency resolve call.
        """
        dependency = trigger(task, *args, **kwargs)
        self.meta_depend(dependency)

    @property
    def meta_type(self):
        """Task's type as a string.
        """
        return type(self).__name__

    # TODO: clean updates list while applying?
    def meta_update(self):
        updates = self.meta_inspect(
            name='updates', lookup=True, default=[])
        for update in updates:
            update.apply(self)

    # Private

    def __init_dependencies(self):
        for dependency in self.__parameters.pop('depend', []):
            self.meta_depend(dependency)
        for task in self.__parameters.pop('require', []):
            self.meta_require(task)
        for task in self.__parameters.pop('trigger', []):
            self.meta_trigger(task)

    def __resolve_dependencies(self, fail=None):
        for dependency in self.meta_dependencies:
            dependency.resolve(fail=fail)

    @contextmanager
    def __change_directory(self):
        if self.meta_chdir:
            buffer = os.path.abspath(os.getcwd())
            os.chdir(self.meta_path())
            yield
            os.chdir(buffer)
        else:
            yield

    # TODO: improve implementation
    def __check_inheritance(self, name):
        if isinstance(self.meta_inherit, list):
            result = False
            for pattern in self.meta_inherit:
                pattern = re.search(
                    r'^(?P<exclude>\!?)'
                    '(?P<content>.*?)'
                    '(?P<wildcard>\*?)$',
                    pattern)
                if pattern.group('wildcard'):
                    match = name.startswith(pattern.group('content'))
                else:
                    match = (name == pattern.group('content'))
                if match:
                    if pattern.group('exclude'):
                        result = False
                    else:
                        result = True
            return result
        return self.meta_inherit
