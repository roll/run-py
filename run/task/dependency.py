from abc import ABCMeta, abstractmethod
from .builder import TaskBuilder
from .method import MethodTask       

class TaskDependency(metaclass=ABCMeta):
    
    #Public
    
    def __init__(self, task, *args, **kwargs):
        self._task = task
        self._args = args
        self._kwargs = kwargs
        self._is_resolved = False
    
    def __call__(self, builder):
        if not isinstance(builder, self._builder_class):
            builder = self._method_task_class(builder)
        self._apply_dependency(builder)
        return builder
        
    def resolve(self, attribute):
        task = getattr(attribute.meta_module, self._task)
        task(*self._args, **self._kwargs)
        self._is_resolved = True

    @property
    def is_resolved(self):
        return self._is_resolved
    
    #Protected
    
    _builder_class = TaskBuilder
    _method_task_class = MethodTask
    
    @abstractmethod
    def _apply_dependency(self, builder):
        pass #pragma: no cover


class require(TaskDependency):
    
    #Protected
    
    def _apply_dependency(self, builder):
        builder.require(self)


class trigger(TaskDependency):
    
    #Protected
    
    def _apply_dependency(self, builder):
        builder.trigger(self)