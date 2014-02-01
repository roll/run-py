from abc import ABCMeta, abstractmethod
from .builder import TaskBuilder
from .method import MethodTask       

class TaskDependency(metaclass=ABCMeta):
    
    #Public
    
    def __init__(self, task, *args, **kwargs):
        if not isinstance(task, list):
            self._dependencies = [task]
        else:
            self._dependencies = task
        self._args = args
        self._kwargs = kwargs
        self._is_resolved = False
    
    def __call__(self, method):
        if not isinstance(method, self._builder_class):
            builder = self._method_task_class(method)
        else:
            builder = method
        self._apply_dependency(builder)
        return builder
    
    def enable(self, task):
        pass
    
    def disable(self, task):
        for dependency in self._dependencies:
            if isinstance(dependency, type(self)):
                dependency.disable(task)
        
    def resolve(self, attribute):
        for dependency in self._dependencies:
            if isinstance(dependency, type(self)):
                dependency.resolve(attribute)
            else:
                task = getattr(attribute.meta_module, dependency)
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