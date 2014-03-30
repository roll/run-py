import os
from contextlib import contextmanager
from abc import abstractmethod
from ..attribute import Attribute
from .dependency import require, trigger
from .metaclass import TaskMetaclass
from .signal import InitiatedTaskSignal, SuccessedTaskSignal, FailedTaskSignal

class Task(Attribute, metaclass=TaskMetaclass):
    
    #Public
        
    def __meta_init__(self, module, *args, **kwargs):
        self._meta_dependencies = []
        self._meta_add_dependencies(kwargs.pop('depend', []))        
        self._meta_add_dependencies(kwargs.pop('require', []), require)
        self._meta_add_dependencies(kwargs.pop('trigger', []), trigger)
        super().__meta_init__(module, *args, **kwargs)
        
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
        self._meta_add_signal('initiated')
        try:
            self._meta_resolve_dependencies()
            try:
                with self._meta_effective_dir():
                    result = self.invoke(*args, **kwargs)
            except Exception:
                self._meta_resolve_dependencies(is_fail=True)
                raise
            self._meta_resolve_dependencies(is_fail=False)
        except Exception:
            self._meta_add_signal('failed')
            raise
        self._meta_add_signal('successed')
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
    _meta_successed_signal_class = SuccessedTaskSignal
    _meta_failed_signal_class = FailedTaskSignal 
    
    def _meta_add_dependencies(self, container, category=None):
        for dependency in container:
            if category and not isinstance(dependency, category):
                dependency = category(dependency)
            self.add_dependency(dependency)
                
    def _meta_resolve_dependencies(self, is_fail=None):
        for dependency in self._meta_dependencies:
            dependency.resolve(is_fail=is_fail)
            
    def _meta_add_signal(self, name):
        signal_class_attr = '_meta_'+name+'_signal_class' 
        signal_class = getattr(self, signal_class_attr)
        signal = signal_class(self)
        self.meta_dispatcher.add_signal(signal)
     
    @contextmanager
    def _meta_effective_dir(self):
        if self.meta_chdir:
            cwd = os.getcwd()
            os.chdir(self.meta_basedir)
            yield
            os.chdir(cwd)
        else:
            yield  