import os
from contextlib import contextmanager
from abc import abstractmethod
from ..attribute import Attribute
from .dependency import require, trigger
from .metaclass import TaskMetaclass
from .signal import InitiatedTaskSignal, ProcessedTaskSignal

class Task(Attribute, metaclass=TaskMetaclass):
    
    #Public
        
    def __meta_init__(self):
        super().__meta_init__()
        kwargs = self._meta_kwargs        
        self._meta_dependencies = []
        self._meta_dispose_dependencies(
            kwargs.pop('depend', []))        
        self._meta_dispose_dependencies(
            kwargs.pop('require', []), require)
        self._meta_dispose_dependencies(
            kwargs.pop('trigger', []), trigger)
        
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
                                     
    @abstractmethod
    def invoke(self, *args, **kwargs):
        pass #pragma: no cover
             
    def depend(self, dependency):
        self.add_dependency(dependency)
           
    def require(self, task, *args, **kwargs):
        dependency = require(task, *args, **kwargs)
        self.add_dependency(dependency)
        
    def trigger(self, task, *args, **kwargs):
        dependency = trigger(task, *args, **kwargs)
        self.add_dependency(dependency)
    
    def add_dependency(self, dependency):
        dependency.bind(self)
        self._meta_dependencies.append(dependency)
             
    def enable_dependency(self, task, category=None):
        for dependency in self._meta_dependencies:
            if not category or isinstance(dependency, category):
                dependency.enable(task)
        
    def disable_dependency(self, task, category=None):
        for dependency in self._meta_dependencies:
            if not category or isinstance(dependency, category):
                dependency.disable(task)
    
    #Protected
    
    _meta_initiated_signal_class = InitiatedTaskSignal
    _meta_processed_signal_class = ProcessedTaskSignal 
    
    def _meta_dispose_dependencies(self, container, category=None):
        for dependency in container:
            if category and not isinstance(dependency, category):
                dependency = category(dependency)
            self.add_dependency(dependency)
                
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