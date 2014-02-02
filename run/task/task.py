import os
from contextlib import contextmanager
from abc import abstractmethod
from .. import dependency
from ..attribute import Attribute
from .metaclass import TaskMetaclass
from .signal import InitiatedTaskSignal, ProcessedTaskSignal

class Task(Attribute, metaclass=TaskMetaclass):
    
    #Public
    
    def __meta_init__(self, args, kwargs):
        super().__meta_init__(args, kwargs)
        self._is_chdir = kwargs.pop('is_chdir', True)        
        self._requires = []
        self._triggers = []
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
            'Attribute "{name}" is task "{task}" and '
            'can be set only to callable value'.
            format(name=self.meta_name, task=self))
    
    def __call__(self, *args, **kwargs):
        self.meta_dispatcher.add_signal(
            self._initiated_signal_class(self))
        self._resolve_dependencies(self._requires)
        with self._effective_dir():
            result = self.invoke(*args, **kwargs)
        self._resolve_dependencies(self._triggers)
        self.meta_dispatcher.add_signal(
            self._processed_signal_class(self))
        return result
        
    def require(self, task, *args, **kwargs):
        self._add_dependency(
            self._requires, 
            self._require_class, 
            task, *args, **kwargs)
        
    def trigger(self, task, *args, **kwargs):
        self._add_dependency(
            self._triggers, 
            self._trigger_class, 
            task, *args, **kwargs)
        
    @abstractmethod
    def invoke(self, *args, **kwargs):
        pass #pragma: no cover
    
    #Protected
    
    _initiated_signal_class = InitiatedTaskSignal
    _processed_signal_class = ProcessedTaskSignal
    _require_class = dependency.require
    _trigger_class = dependency.trigger
            
    def _add_dependency(self, lst, cls, task, *args, **kwargs):
        if kwargs.pop('is_enable', False):
            for dependency in lst:
                dependency.enable(task)
        elif kwargs.pop('is_disable', False):
            for dependency in lst:
                dependency.disable(task)
        else:
            if not isinstance(task, cls):
                dependency = cls(task, *args, **kwargs)
            else:
                dependency = task
            lst.append(dependency)
    
    def _resolve_dependencies(self, lst):
        for dependency in lst:
            if dependency.is_resolved:
                continue
            dependency.resolve(self)
     
    @contextmanager       
    def _effective_dir(self):
        if self._is_chdir:
            cwd = os.getcwd()
            os.chdir(self.meta_basedir)
            yield
            os.chdir(cwd)
        else:
            yield  