import os
import inspect
from copy import copy
from abc import abstractmethod
from contextlib import contextmanager
from ..dependency import Predecessor, Successor, require, trigger
from ..settings import settings
from .metaclass import TaskMetaclass
from .signal import InitiatedTaskSignal, SuccessedTaskSignal, FailedTaskSignal


class Task(Predecessor, Successor, metaclass=TaskMetaclass):

    # Public

    @classmethod
    def __meta_create__(cls, *args, meta_module, meta_updates, **kwargs):
        # Create task object
        self = object.__new__(cls)
        # Initiate module, updates
        self._meta_module = meta_module
        self._meta_updates = meta_updates
        # Initiate params
        self._meta_params = {}
        for key in list(kwargs):
            if key.startswith('meta_'):
                name = key.replace('meta_', '')
                self._meta_params[name] = kwargs.pop(key)
        # Initiate directory
        self._meta_initial_dir = os.path.abspath(os.getcwd())
        # Initiate dependencies
        self._meta_dependencies = []
        self._meta_init_dependencies()
        # Initiate arguments
        self._meta_args = ()
        self._meta_kwargs = {}
        # Call user init
        self.__init__(*args, **kwargs)
        return self

    def __meta_update__(self):
        for update in self._meta_updates:
            update.apply(self)

    def __init__(self, *args, **kwargs):
        self._meta_args = args
        self._meta_kwargs = kwargs

    def __call__(self, *args, **kwargs):
        self._meta_add_signal('initiated')
        try:
            self._meta_resolve_dependencies()
            try:
                result = self.meta_effective_invoke(*args, **kwargs)
            except Exception:
                if self.meta_fallback is not None:
                    result = self.meta_fallback
                else:
                    self._meta_resolve_dependencies(failed=True)
                    raise
            self._meta_resolve_dependencies(failed=False)
        except Exception:
            self._meta_add_signal('failed')
            raise
        self._meta_add_signal('successed')
        return result

    def __repr__(self):
        return ('<{self.meta_type} "{self.meta_qualname}">'.
                format(self=self))

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
        return self._meta_params.get(
            'basedir', self.meta_module.meta_basedir)

    @meta_basedir.setter
    def meta_basedir(self, value):
        self._meta_params['basedir'] = value

    @property
    def meta_chdir(self):
        """Task's chdir status (enabled or disabled).

        .. seealso:: :attr:`run.Task.meta_basedir`

        This property is:

        - initable/writable
        - inherited from module
        """
        return self._meta_params.get(
            'chdir', self.meta_module.meta_chdir)

    @meta_chdir.setter
    def meta_chdir(self, value):
        self._meta_params['chdir'] = value

    @property
    def meta_color_name(self):
        name = self.meta_name
        if not self.meta_grayscale:
            name = '\033[' + self._meta_color_code + name + '\033[0m'
        return name

    @property
    def meta_color_qualname(self):
        qualname = self.meta_qualname
        if not self.meta_grayscale:
            qualname = '\033[' + self._meta_color_code + qualname + '\033[0m'
        return qualname

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

    def meta_disable_dependency(self, task, *, types=None):
        """Disable all dependencies for the task.
        """
        for dependency in self.meta_dependencies:
            if types is not None:
                if not isinstance(dependency, tuple(types)):
                    continue
            task = self.meta_module.meta_lookup(task)
            if dependency.predecessor is task:
                dependency.disable()

    @property
    def meta_dispatcher(self):
        """Task's dispatcher.

        Dispatcher used to operate signals.

        This property is:

        - initable/writable
        - inherited from module
        """
        return self._meta_params.get(
            'dispatcher', self.meta_module.meta_dispatcher)

    @meta_dispatcher.setter
    def meta_dispatcher(self, value):
        self._meta_params['dispatcher'] = value

    @property
    def meta_docstring(self):
        """Task's docstring.

        This property is:

        - initable/writable
        """
        return self._meta_params.get(
            'docstring', str(inspect.getdoc(self)).strip())

    @meta_docstring.setter
    def meta_docstring(self, value):
        self._meta_params['docstring'] = value

    @contextmanager
    def meta_effective_dir(self):
        if self.meta_chdir:
            previous_dir = os.path.abspath(os.getcwd())
            following_dir = os.path.join(
                self._meta_initial_dir, self.meta_basedir)
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

    def meta_enable_dependency(self, task, types=None):
        """Enable all dependencies for the task.
        """
        for dependency in self.meta_dependencies:
            if types is not None:
                if not isinstance(dependency, tuple(types)):
                    continue
            task = self.meta_module.meta_lookup(task)
            if dependency.predecessor is task:
                dependency.enable()

    @property
    def meta_fallback(self):
        """Task's fallback.

        Fallback used when task invocation fails.

        This property is:

        - initable/writable
        - inherited from module
        """
        return self._meta_params.get(
            'fallback', self.meta_module.meta_fallback)

    @meta_fallback.setter
    def meta_fallback(self, value):
        self._meta_params['fallback'] = value

    @property
    def meta_grayscale(self):
        """Task's grayscale flag (grayscale or not).

        This property is:

        - initable/writable
        - inherited from module
        """
        return self._meta_params.get(
            'grayscale', self.meta_module.meta_grayscale)

    @meta_grayscale.setter
    def meta_grayscale(self, value):
        self._meta_params['grayscale'] = value

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
    def meta_params(self):
        return self._meta_params

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
                self._meta_default_main_module_name):
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
        dependency = self._meta_require(task, *args, **kwargs)
        self.meta_depend(dependency)

    @property
    def meta_signature(self):
        """Task's signature.

        This property is:

        - initable/writable
        """
        return self._meta_params.get(
            'signature', str(inspect.signature(self.meta_invoke)))

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
        return self._meta_params.get(
            'strict', self.meta_module.meta_strict)

    @meta_strict.setter
    def meta_strict(self, value):
        self._meta_params['strict'] = value

    def meta_trigger(self, task, *args, **kwargs):
        """Add trigger dependency.
        """
        dependency = self._meta_trigger(task, *args, **kwargs)
        self.meta_depend(dependency)

    @property
    def meta_type(self):
        """Task's type as a string.
        """
        return type(self).__name__

    # Protected

    _meta_color_code = settings.task_color_code
    _meta_default_main_module_name = settings.main_module_name
    _meta_FailedTaskSignal = FailedTaskSignal
    _meta_InitiatedTaskSignal = InitiatedTaskSignal
    _meta_require = require
    _meta_SuccessedTaskSignal = SuccessedTaskSignal
    _meta_trigger = trigger

    def _meta_init_dependencies(self):
        for dependency in self._meta_params.get('depend', []):
            self.meta_depend(dependency)
        for task in self._meta_params.get('require', []):
            self.meta_require(task)
        for task in self._meta_params.get('trigger', []):
            self.meta_trigger(task)

    def _meta_resolve_dependencies(self, failed=None):
        for dependency in self.meta_dependencies:
            dependency.resolve(failed=failed)

    def _meta_add_signal(self, name):
        attribute_name = '_meta_' + name.capitalize() + 'TaskSignal'
        Signal = getattr(self, attribute_name)
        signal = Signal(self)
        self.meta_dispatcher.add_signal(signal)
