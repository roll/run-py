import os
from contextlib import contextmanager
from collections import OrderedDict
from abc import abstractmethod
from ..attribute import Attribute
from .dependency import TaskDependency
from .metaclass import TaskMetaclass
from .signal import InitiatedTaskSignal, ProcessedTaskSignal

class Task(Attribute, metaclass=TaskMetaclass):
    
    #Public
    
    def __meta_init__(self, args, kwargs):
        super().__meta_init__(args, kwargs)
        self._requirments = OrderedDict()
        self._triggers = OrderedDict()
        self._is_chdir = kwargs.pop('is_chdir', True)        
        self.require(kwargs.pop('require', []))
        self.trigger(kwargs.pop('trigger', []))
        
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
        self._resolve_requirements()
        with self._effective_dir():
            result = self.invoke(*args, **kwargs)
        self._resolve_triggers()
        self.meta_dispatcher.add_signal(
            self._processed_signal_class(self))
        return result
        
    def require(self, tasks, disable=False):
        self._update_dependencies(self._requirments, tasks, disable)
        
    def trigger(self, tasks, disable=False):
        self._update_dependencies(self._triggers, tasks, disable)
        
    @abstractmethod
    def invoke(self, *args, **kwargs):
        pass #pragma: no cover
    
    #Protected
    
    _initiated_signal_class = InitiatedTaskSignal
    _processed_signal_class = ProcessedTaskSignal    
    _dependency_class = TaskDependency
            
    def _resolve_requirements(self):
        for dependency in self._requirments.values():
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
        
    def _resolve_triggers(self):
        for dependency in self._triggers.values():
            dependency.resolve(self)
        
            
    @classmethod
    def _update_dependencies(cls, group, tasks, disable=False):
        for task in tasks:
            dependency = cls._dependency_class(task)
            if disable:
                group.pop(dependency.name, None)
            else:
                if dependency.name not in group:
                    group[dependency.name] = dependency    