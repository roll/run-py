import os
import inspect
from copy import copy
from box.importlib import inject
from contextlib import contextmanager
from abc import ABCMeta, abstractmethod
from ..attribute import Attribute
from .module import module
from .signal import InitiatedTaskSignal, SuccessedTaskSignal, FailedTaskSignal

class Task(Attribute, metaclass=ABCMeta):

    # Public

    def __build__(self, module, *args, **kwargs):
        self._meta_args = ()
        self._meta_kwargs = {}
        self._meta_dependencies = []
        self._add_dependencies(kwargs.pop('depend', []))
        self._add_dependencies(kwargs.pop('require', []), self._require)
        self._add_dependencies(kwargs.pop('trigger', []), self._trigger)
        self._initial_dir = os.path.abspath(os.getcwd())
        super().__build__(module, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        self._meta_args = args
        self._meta_kwargs = kwargs

    def __get__(self, module, module_class=None):
        return self

    def __set__(self, module, value):
        if callable(value):
            self.invoke = value
        else:
            raise TypeError(
            'Attribute is task "{task}" and '
            'can be set only to callable value'.
            format(task=self))

    def __call__(self, *args, **kwargs):
        self._add_signal('initiated')
        try:
            self._resolve_dependencies()
            try:
                result = self.effective_invoke(*args, **kwargs)
            except Exception:
                if self.meta_fallback != None:
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

    @property
    def meta_dependencies(self):
        """Task's list of dependencies.
        """
        return self._meta_dependencies

    @property
    def meta_fallback(self):
        """Task's fallback.

        Fallback used when attribute invocation fails.

        This property is:

        - initable/writable
        - inherited from module
        """
        return self._meta_params.get('fallback',
            self.meta_module.meta_fallback)

    @meta_fallback.setter
    def meta_fallback(self, value):
        self._meta_params['fallback'] = value

    @property
    def meta_kwargs(self):
        """Tasks's default keyword arguments
        """
        return self._meta_kwargs

    @property
    def meta_signature(self):
        """Task's signature.

        This property is:

        - initable/writable
        """
        return self._meta_params.get('signature',
            str(inspect.signature(self.invoke)))

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

    def depend(self, dependency):
        """Add custom dependency.
        """
        dependency.bind(self)
        self.meta_dependencies.append(dependency)

    def require(self, task, *args, **kwargs):
        """Add require dependency.
        """
        dependency = self._require(task, *args, **kwargs)
        self.depend(dependency)

    def trigger(self, task, *args, **kwargs):
        """Add trigger dependency.
        """
        dependency = self._trigger(task, *args, **kwargs)
        self.depend(dependency)

    def enable_dependency(self, task, category=None):
        """Enable all dependencies for the task.
        """
        for dependency in self.meta_dependencies:
            if category == None or self._isinstance(dependency, category):
                if dependency.task == task:
                    dependency.enable()

    def disable_dependency(self, task, category=None):
        """Disable all dependencies for the task.
        """
        for dependency in self.meta_dependencies:
            if category == None or self._isinstance(dependency, category):
                if dependency.task == task:
                    dependency.disable()

    def effective_invoke(self, *args, **kwargs):
        """Invoke task with effective dir, args and kwargs.
        """
        with self._effective_dir():
            return self.invoke(
                *self._effective_args(*args),
                **self._effective_kwargs(**kwargs))

    @abstractmethod
    def invoke(self, *args, **kwargs):
        """Invoke task.
        """
        pass  # pragma: no cover

    # Protected

    _failed_signal_class = FailedTaskSignal
    _initiated_signal_class = InitiatedTaskSignal
    _isinstance = staticmethod(isinstance)
    _module = module
    _require = inject('require', module='run.dependency')
    _successed_signal_class = SuccessedTaskSignal
    _trigger = inject('trigger', module='run.dependency')


    def _add_dependencies(self, container, category=None):
        for dependency in container:
            if category and not self._isinstance(dependency, category):
                dependency = category(dependency)
            self.depend(dependency)

    def _resolve_dependencies(self, failed=None):
        for dependency in self.meta_dependencies:
            dependency.resolve(failed=failed)

    def _add_signal(self, name):
        signal_class_attr = '_' + name + '_signal_class'
        signal_class = getattr(self, signal_class_attr)
        signal = signal_class(self)
        self.meta_dispatcher.add_signal(signal)

    @contextmanager
    def _effective_dir(self):
        if self.meta_chdir:
            previous_dir = os.path.abspath(os.getcwd())
            following_dir = os.path.join(
                self._initial_dir, self.meta_basedir)
            os.chdir(following_dir)
            yield
            os.chdir(previous_dir)
        else:
            yield

    def _effective_args(self, *args):
        eargs = self.meta_args + args
        eargs = tuple(map(self._expand_arg, eargs))
        return eargs

    def _effective_kwargs(self, **kwargs):
        ekwargs = copy(self.meta_kwargs)
        ekwargs.update(kwargs)
        for key, value in ekwargs.items():
            ekwargs[key] = self._expand_arg(value)
        return ekwargs

    def _expand_arg(self, value):
        result = value
        if self._isinstance(value, self._module):
            result = value.expand(self.meta_module)
        return result
