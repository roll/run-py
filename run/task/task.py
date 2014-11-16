import os
import uuid
import inspect
from copy import copy
from functools import partial
from contextlib import contextmanager
from sugarbowl import merge_dicts
from ..settings import settings
from .metaclass import Metaclass
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

    def __call__(self, *args, **kwargs):
        Event = CallTaskEvent
        uid = uuid.uuid4().int
        args = self.meta_args + args
        kwargs = merge_dicts(self.meta_kwargs, kwargs)
        pEvent = partial(Event, self, uid=uid, args=args, kwargs=kwargs)
        self.meta_notify(pEvent(state=Event.INIT))
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
            self.meta_notify(pEvent(state=Event.FAIL))
            raise
        self.meta_notify(pEvent(state=Event.DONE))
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
        return self.meta_inspect('basedir', default=None)

    @property
    def meta_chdir(self):
        """Task's chdir status (enabled or disabled).

        .. seealso:: :attr:`run.Task.meta_basedir`
        """
        return self.meta_inspect(
            'chdir', module=True, default=settings.chdir)

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
        self.__initdir = os.path.abspath(os.getcwd())
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
            'docstring', default=str(inspect.getdoc(self)).strip())

    @property
    def meta_fallback(self):
        """Task's fallback.

        Fallback used when task invocation fails.
        """
        return self.meta_inspect(
            'fallback', module=True, default=settings.fallback)

    @property
    def meta_hidden(self):
        return self.meta_inspect('hidden', default=False)

    def meta_inspect(self, name, *, module=False, default=None):
        """Return meta parameter
        """
        if name in self.__parameters:
            return self.__parameters[name]
        if module and self.meta_module:
            return self.meta_module.meta_inspect(name, default=default)
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
    def meta_kwargs(self):
        """Tasks's default keyword arguments.
        """
        return self.__kwargs

    @property
    def meta_listeners(self):
        return self.meta_inspect('listeners', default=[])

    def meta_locate(self, *paths):
        basedir = self.meta_basedir
        if basedir is None or not os.path.isabs(basedir):
            prefix = self.__initdir
            if self.meta_module:
                prefix = self.meta_module.meta_locate()
            basedir = os.path.join(*filter(None, [prefix, basedir]))
        path = os.path.join(basedir, *paths)
        return path

    @property
    def meta_module(self):
        """Task's module.
        """
        return self.meta_inspect('module', default=None)

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

    def meta_not_depend(self, target):
        """Remove all of task dependencies.

        Parameters
        ----------
        task: str
            Task name to be not dependent upon.
        """
        predecessor = getattr(self.meta_module, target)
        for dependency in copy(self.meta_dependencies):
            if dependency.predecessor is predecessor:
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

    def meta_require(self, __target, *args, **kwargs):
        """Add require dependency.

        Parameters
        ----------
        task: str
            Task name to require.
        args, kwargs
            Arguments for dependency resolve call.
        """
        dependency = require(__target, *args, **kwargs)
        self.meta_depend(dependency)

    @property
    def meta_signature(self):
        """Task's signature.
        """
        return self.meta_inspect(
            'signature', default=str(inspect.signature(self.meta_invoke)))

    @property
    def meta_style(self):
        return self.meta_inspect('style', default='task')

    @property
    def meta_top(self):
        if self.meta_module:
            self.meta_module.meta_top
        else:
            return self

    def meta_trigger(self, __target, *args, **kwargs):
        """Add trigger dependency.

        Parameters
        ----------
        task: str
            Task name to trigger.
        args, kwargs
            Arguments for dependency resolve call.
        """
        dependency = trigger(__target, *args, **kwargs)
        self.meta_depend(dependency)

    @property
    def meta_type(self):
        """Task's type as a string.
        """
        return type(self).__name__

    # TODO: clean updates list while applying?
    def meta_update(self):
        updates = self.meta_inspect('updates', default=[])
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
        if not self.meta_chdir:
            yield
            return
        oldpath = os.path.abspath(os.getcwd())
        newpath = self.meta_locate()
        if oldpath == newpath:
            yield
            return
        os.chdir(newpath)
        yield
        os.chdir(oldpath)
