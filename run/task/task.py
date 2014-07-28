import os
import inspect
from copy import copy
from abc import abstractmethod
from contextlib import contextmanager
from ..dependency import require, trigger
from ..settings import settings
from .metaclass import TaskMetaclass
from .signal import InitiatedTaskSignal, SuccessedTaskSignal, FailedTaskSignal

class Task(metaclass=TaskMetaclass):

    # Public

    # TODO: we can't use module keyword in kwargs (also cls, updated?)
    def __build__(self, module, *args, **kwargs):
        self._meta_module = module
        self._meta_args = ()
        self._meta_kwargs = {}
        self._meta_dependencies = []
        self._initial_dir = os.path.abspath(os.getcwd())
        # Collect meta params
        self._meta_params = {}
        for key in list(kwargs):
            if key.startswith('meta_'):
                name = key.replace('meta_', '')
                self._meta_params[name] = kwargs.pop(key)
        # Complete building
        self._init_dependencies()
        self.__init__(*args, **kwargs)
        self._meta_builded = True

    def __init__(self, *args, **kwargs):
        self._meta_args = args
        self._meta_kwargs = kwargs

    def __call__(self, *args, **kwargs):
        self._add_signal('initiated')
        try:
            self._resolve_dependencies()
            try:
                result = self.meta_effective_invoke(*args, **kwargs)
            except Exception:
                if self.meta_fallback is not None:
                    result = self.meta_fallback
                else:
                    self._resolve_dependencies(failed=True)
                    raise
            self._resolve_dependencies(failed=False)
        except Exception:
            self._add_signal('failed')
            raise
        self._add_signal('successed')
        return result

    def __repr__(self):
        if self.meta_builded:
            return ('<{self.meta_type} "{self.meta_qualname}">'.
                    format(self=self))
        return super().__repr__()

    @property
    def meta_args(self):
        """Tasks's default arguments
        """
        return self._meta_args

    @property
    def meta_basedir(self):
        """Task's basedir.

        If meta_chdir is True current directory will be
        changed to meta_basedir when task invoking.

        This property is:

        - initable/writable
        - inherited from module
        """
        return self._meta_params.get('basedir',
           self.meta_module.meta_basedir)

    @meta_basedir.setter
    def meta_basedir(self, value):
        self._meta_params['basedir'] = value

    @property
    def meta_builded(self):
        """Build status of task (builded or not).

        Task is builded after succefull __build__ call.
        It includes some internal building and __init__ call.
        """
        return vars(self).get('_meta_builded', False)

    @property
    def meta_chdir(self):
        """Task's chdir status (enabled or disabled).

        .. seealso:: :attr:`run.Task.meta_basedir`

        This property is:

        - initable/writable
        - inherited from module
        """
        return self._meta_params.get('chdir',
            self.meta_module.meta_chdir)

    @meta_chdir.setter
    def meta_chdir(self, value):
        self._meta_params['chdir'] = value

    def meta_depend(self, dependency):
        """Add custom dependency.
        """
        dependency.bind(self)
        self.meta_dependencies.append(dependency)

    @property
    def meta_dependencies(self):
        """Task's list of dependencies.
        """
        return self._meta_dependencies

    def meta_disable_dependency(self, task, category=None):
        """Disable all dependencies for the task.
        """
        for dependency in self.meta_dependencies:
            if category is None or self._isinstance(dependency, category):
                if dependency.task == task:
                    dependency.disable()

    @property
    def meta_dispatcher(self):
        """Task's dispatcher.

        Dispatcher used to operate signals.

        This property is:

        - initable/writable
        - inherited from module
        """
        return self._meta_params.get('dispatcher',
            self.meta_module.meta_dispatcher)

    @meta_dispatcher.setter
    def meta_dispatcher(self, value):
        self._meta_params['dispatcher'] = value

    @property
    def meta_docstring(self):
        """Task's docstring.

        This property is:

        - initable/writable
        """
        return self._meta_params.get('docstring',
            str(inspect.getdoc(self)).strip())

    @meta_docstring.setter
    def meta_docstring(self, value):
        self._meta_params['docstring'] = value

    @contextmanager
    def meta_effective_dir(self):
        if self.meta_chdir:
            previous_dir = os.path.abspath(os.getcwd())
            following_dir = os.path.join(
                self._initial_dir, self.meta_basedir)
            os.chdir(following_dir)
            yield
            os.chdir(previous_dir)
        else:
            yield

    def meta_effective_invoke(self, *args, **kwargs):
        """Invoke task with effective dir, args and kwargs.
        """
        eargs = self.meta_args + args
        ekwargs = copy(self.meta_kwargs)
        ekwargs.update(kwargs)
        with self.meta_effective_dir():
            return self.meta_invoke(*eargs, **ekwargs)

    def meta_enable_dependency(self, task, category=None):
        """Enable all dependencies for the task.
        """
        for dependency in self.meta_dependencies:
            if category is None or self._isinstance(dependency, category):
                if dependency.task == task:
                    dependency.enable()

    @property
    def meta_fallback(self):
        """Task's fallback.

        Fallback used when task invocation fails.

        This property is:

        - initable/writable
        - inherited from module
        """
        return self._meta_params.get('fallback',
            self.meta_module.meta_fallback)

    @meta_fallback.setter
    def meta_fallback(self, value):
        self._meta_params['fallback'] = value

    @abstractmethod
    def meta_invoke(self, *args, **kwargs):
        """Invoke task.
        """
        pass  # pragma: no cover

    @property
    def meta_kwargs(self):
        """Tasks's default keyword arguments
        """
        return self._meta_kwargs

    @property
    def meta_main_module(self):
        """Task's main module of module hierarchy.
        """
        return self.meta_module.meta_main_module

    @property
    def meta_module(self):
        """Task's module.
        """
        return self._meta_module

    @property
    def meta_name(self):
        """Task's name.

        Name is defined as task name in module.
        If module is None name will be empty string.
        """
        name = ''
        tasks = self.meta_module.meta_tasks
        for key, task in tasks.items():
            if task is self:
                name = key
        return name

    @property
    def meta_qualname(self):
        """Task's qualified name.

        Qualname is full task name in hierarhy
        starts from main module.
        """
        if self.meta_module.meta_is_main_module:
            if (self.meta_module.meta_name ==
                self._default_meta_main_module_name):
                pattern = '{name}'
            else:
                pattern = '[{module_qualname}] {name}'
        else:
            pattern = '{module_qualname}.{name}'
        return pattern.format(
            module_qualname=self.meta_module.meta_qualname,
            name=self.meta_name)

    def meta_require(self, task, *args, **kwargs):
        """Add require dependency.
        """
        dependency = self._require(task, *args, **kwargs)
        self.meta_depend(dependency)

    @property
    def meta_signature(self):
        """Task's signature.

        This property is:

        - initable/writable
        """
        return self._meta_params.get('signature',
            str(inspect.signature(self.meta_invoke)))

    @meta_signature.setter
    def meta_signature(self, value):
        self._meta_params['signature'] = value

    @property
    def meta_strict(self):
        """Task's strict mode status (enabled or disabled).

        This property is:

        - initable/writable
        - inherited from module
        """
        return self._meta_params.get('strict',
            self.meta_module.meta_strict)

    @meta_strict.setter
    def meta_strict(self, value):
        self._meta_params['strict'] = value

    def meta_trigger(self, task, *args, **kwargs):
        """Add trigger dependency.
        """
        dependency = self._trigger(task, *args, **kwargs)
        self.meta_depend(dependency)

    @property
    def meta_type(self):
        """Task's type as a string.
        """
        return type(self).__name__

    # Protected

    _default_meta_main_module_name = settings.default_meta_main_module_name
    _failed_signal_class = FailedTaskSignal
    _initiated_signal_class = InitiatedTaskSignal
    _isinstance = staticmethod(isinstance)
    _require = require
    _successed_signal_class = SuccessedTaskSignal
    _trigger = trigger

    def _init_dependencies(self):
        for dependency in self._meta_params.get('depend', []):
            self.meta_depend(dependency)
        for task in self._meta_params.get('require', []):
            self.meta_require(task)
        for task in self._meta_params.get('trigger', []):
            self.meta_trigger(task)

    def _resolve_dependencies(self, failed=None):
        for dependency in self.meta_dependencies:
            dependency.resolve(failed=failed)

    def _add_signal(self, name):
        signal_class_attr = '_' + name + '_signal_class'
        signal_class = getattr(self, signal_class_attr)
        signal = signal_class(self)
        self.meta_dispatcher.add_signal(signal)
