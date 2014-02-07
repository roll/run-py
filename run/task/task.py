import os
from contextlib import contextmanager
from abc import abstractmethod
from ..attribute import Attribute
from .dependency import require, trigger
from .metaclass import TaskMetaclass
from .signal import InitiatedTaskSignal, ProcessedTaskSignal

class Task(Attribute, metaclass=TaskMetaclass):
    
    #Public
        
    def __system_init__(self):
        super().__system_init__()
        kwargs = self.__system_kwargs__        
        self._meta_dependencies = []
        for dependency in kwargs.pop('require', []):
            self.require(dependency)
        for dependency in kwargs.pop('trigger', []):
            self.trigger(dependency)
        
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
        self.meta_dispatcher.add_signal(
            self._meta_initiated_signal_class(self))
        self._meta_resolve_dependencies()
        with self._meta_effective_dir():
            result = self.invoke(*args, **kwargs)
        self._meta_resolve_dependencies(after=True)
        self.meta_dispatcher.add_signal(
            self._meta_processed_signal_class(self))
        return result
    
    @property
    def meta_dependencies(self):
        return self._meta_dependencies
       
    def require(self, task, *args, **kwargs):
        self._meta_depend(require, task, *args, **kwargs)
        
    def trigger(self, task, *args, **kwargs):
        self._meta_depend(trigger, task, *args, **kwargs)
        
    @abstractmethod
    def invoke(self, *args, **kwargs):
        pass #pragma: no cover
    
    #Protected
    
    _meta_initiated_signal_class = InitiatedTaskSignal
    _meta_processed_signal_class = ProcessedTaskSignal
    
    def _meta_depend(self, cls, task, *args, **kwargs):
        if kwargs.pop('is_enable', False):
            self._meta_enable_dependency(cls, task)
        elif kwargs.pop('is_disable', False):
            self._meta_disable_dependency(cls, task)
        else:
            self._meta_add_dependency(cls, task, *args, **kwargs)
               
    def _meta_add_dependency(self, cls, task, *args, **kwargs):
            if not isinstance(task, cls):
                dependency = cls(task, *args, **kwargs)
            else:
                dependency = task
            dependency.bind(self.meta_module)
            self._meta_dependencies.append(dependency)
    
    def _meta_enable_dependency(self, cls, task):
        for dependency in self._meta_dependencies:
            if isinstance(dependency, cls):
                dependency.enable(task)
            
    def _meta_disable_dependency(self, cls, task):
        for dependency in self._meta_dependencies:
            if isinstance(dependency, cls):
                dependency.disable(task)     
            
    def _meta_resolve_dependencies(self, after=False):
        for dependency in self._meta_dependencies:
            dependency.resolve(after=after)
     
    @contextmanager       
    def _meta_effective_dir(self):
        if self.meta_is_chdir:
            cwd = os.getcwd()
            os.chdir(self.meta_basedir)
            yield
            os.chdir(cwd)
        else:
            yield  