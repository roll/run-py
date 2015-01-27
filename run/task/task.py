import os
import uuid
import inspect
from copy import copy
from functools import partial
from contextlib import contextmanager
from ..helpers import merge_dicts
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
        args = self.Args + args
        kwargs = merge_dicts(self.Kwargs, kwargs)
        pEvent = partial(Event, self, uid=uid, args=args, kwargs=kwargs)
        self.Notify(pEvent(state=Event.INIT))
        try:
            self.__resolve_dependencies()
            try:
                with self.__change_directory():
                    result = self.Invoke(*args, **kwargs)
            except Exception:
                if self.Fallback is not None:
                    result = self.Fallback
                else:
                    self.__resolve_dependencies(fail=True)
                    raise
            self.__resolve_dependencies(fail=False)
        except Exception:
            self.Notify(pEvent(state=Event.FAIL))
            raise
        self.Notify(pEvent(state=Event.DONE))
        return result

    def __repr__(self):
        template = '<{self.Type}>'
        if self.Qualname:
            template = '<{self.Type} "{self.Qualname}">'
        return template.format(self=self)

    @property
    def Args(self):
        """Tasks's default arguments
        """
        return self.__args

    @property
    def Basedir(self):
        """Task's basedir.

        If Chdir is True current directory will be
        changed to Basedir when task invoking.
        """
        return self.Inspect('Basedir', default=None)

    @property
    def Chdir(self):
        """Task's chdir status (enabled or disabled).

        .. seealso:: :attr:`run.Task.Basedir`
        """
        return self.Inspect(
            'Chdir', module=True, default=settings.chdir)

    @classmethod
    def Create(cls, *args, **kwargs):
        # Create task object
        self = object.__new__(cls)
        # Initiate parameters
        self.__parameters = {}
        for key in list(kwargs):
            if key[0].isupper():
                self.__parameters[key] = kwargs.pop(key)
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

    def Depend(self, dependency):
        """Add custom dependency.

        Parameters
        ----------
        dependency: :class:`.dependency.Dependency`
            Dependency to be dependent upon.
        """
        dependency.bind(self)
        self.Dependencies.append(dependency)

    @property
    def Dependencies(self):
        """Task's list of dependencies.
        """
        return self.__dependencies

    @property
    def Docstring(self):
        """Task's docstring.
        """
        return self.Inspect(
            'Docstring', default=str(inspect.getdoc(self)).strip())

    @property
    def Fallback(self):
        """Task's fallback.

        Fallback used when task invocation fails.
        """
        return self.Inspect(
            'Fallback', module=True, default=settings.fallback)

    @property
    def Hidden(self):
        return self.Inspect('Hidden', default=False)

    def Inspect(self, name, *, module=False, default=None):
        """Return meta parameter
        """
        if name in self.__parameters:
            return self.__parameters[name]
        if module and self.Module:
            return self.Module.Inspect(name, default=default)
        return default

    def Invoke(self, *args, **kwargs):
        """Invoke task.

        Parameters
        ----------
        args, kwargs
            Arguments for task invokation.
        """
        pass

    @property
    def Kwargs(self):
        """Tasks's default keyword arguments.
        """
        return self.__kwargs

    @property
    def Listeners(self):
        return self.Inspect('Listeners', default=[])

    def Locate(self, *paths):
        basedir = self.Basedir
        if basedir is None or not os.path.isabs(basedir):
            prefix = self.__initdir
            if self.Module:
                prefix = self.Module.Locate()
            basedir = os.path.join(*filter(None, [prefix, basedir]))
        path = os.path.join(basedir, *paths)
        return path

    @property
    def Module(self):
        """Task's module.
        """
        return self.Inspect('Module', default=None)

    @property
    def Name(self):
        """Task's name.

        Name is defined as task name in module.
        """
        name = ''
        if self.Module:
            tasks = self.Module.Tasks
            for key, task in tasks.items():
                if task is self:
                    name = key
        return name

    def NotDepend(self, target):
        """Remove all of task dependencies.

        Parameters
        ----------
        task: str
            Task name to be not dependent upon.
        """
        predecessor = getattr(self.Module, target)
        for dependency in copy(self.Dependencies):
            if dependency.predecessor is predecessor:
                self.Dependencies.remove(dependency)

    # TODO: add event flow management (like stop propognation)
    def Notify(self, event):
        for listener in self.Listeners:
            listener(event)
        if self.Module:
            self.Module.Notify(event)

    @property
    def Qualname(self):
        qualname = ''
        if self.Module:
            qualname = '.'.join(filter(None,
                [self.Module.Qualname, self.Name]))
        return qualname

    def Require(self, __target, *args, **kwargs):
        """Add require dependency.

        Parameters
        ----------
        task: str
            Task name to require.
        args, kwargs
            Arguments for dependency resolve call.
        """
        dependency = require(__target, *args, **kwargs)
        self.Depend(dependency)

    @property
    def Signature(self):
        """Task's signature.
        """
        return self.Inspect(
            'Signature', default=str(inspect.signature(self.Invoke)))

    @property
    def Style(self):
        return self.Inspect('Style', default='task')

    @property
    def Top(self):
        if self.Module:
            return self.Module.Top
        else:
            return self

    def Trigger(self, __target, *args, **kwargs):
        """Add trigger dependency.

        Parameters
        ----------
        task: str
            Task name to trigger.
        args, kwargs
            Arguments for dependency resolve call.
        """
        dependency = trigger(__target, *args, **kwargs)
        self.Depend(dependency)

    @property
    def Type(self):
        """Task's type as a string.
        """
        return type(self).__name__

    # TODO: clean updates list while applying?
    def Update(self):
        updates = self.Inspect('Updates', default=[])
        for update in updates:
            update.apply(self)

    # Private

    def __init_dependencies(self):
        for dependency in self.__parameters.pop('Depend', []):
            self.Depend(dependency)
        for task in self.__parameters.pop('Require', []):
            self.Require(task)
        for task in self.__parameters.pop('Trigger', []):
            self.Trigger(task)

    def __resolve_dependencies(self, fail=None):
        for dependency in self.Dependencies:
            dependency.resolve(fail=fail)

    @contextmanager
    def __change_directory(self):
        if not self.Chdir:
            yield
            return
        oldpath = os.path.abspath(os.getcwd())
        newpath = self.Locate()
        if oldpath == newpath:
            yield
            return
        os.chdir(newpath)
        yield
        os.chdir(oldpath)
