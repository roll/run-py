from abc import ABCMeta, abstractmethod
from .builder import TaskBuilder

class TaskDependency(metaclass=ABCMeta):
    
    #Public
    
    def __init__(self, task, *args, **kwargs):
        if not isinstance(task, list):
            self._is_composite = False
            self._task = task
        else:
            self._is_composite = True
            self._dependencies = []
            for dependency in task:
                if not isinstance(task, type(self)):
                    dependency = type(self)(dependency, *args, **kwargs)
                self._dependencies.append(dependency)
        self._args = args
        self._kwargs = kwargs
        self._enabled = True
        self._resolves = 0
    
    def __call__(self, method):
        if not isinstance(method, self._builder_class):
            builder = self._method_task_class(method)
        else:
            builder = method
        self._add_dependency(builder)
        return builder
    
    def enable(self, task):
        if not self._is_composite:
            self._enabled = True
        else:
            for dependency in self._dependencies:
                dependency.enable(task)
    
    def disable(self, task):
        if not self._is_composite:
            self._enabled = False
        else:
            for dependency in self._dependencies:
                dependency.disable(task)
        
    def resolve(self, attribute):
        if not self._is_composite:
            task = getattr(attribute.meta_module, self._task)
            task(*self._args, **self._kwargs)
        else:       
            for dependency in self._dependencies:
                dependency.resolve(attribute)
        self._resolves += 1

    @property
    @abstractmethod
    def is_resolved(self):
        pass #pragma: no cover
    
    #Protected
    
    _builder_class = TaskBuilder
    
    @property
    def _method_task_class(self):
        #Cycle dependency if static
        from .method import MethodTask    
        return MethodTask
    
    @abstractmethod
    def _add_dependency(self, builder):
        pass #pragma: no cover

    
class require(TaskDependency):
    
    #Public
    
    @property
    def is_resolved(self):
        return bool(self._resolves)    
    
    #Protected
    
    def _add_dependency(self, builder):
        builder.require(self)


class trigger(TaskDependency):
    
    #Public
    
    @property
    def is_resolved(self):
        return False
    
    #Protected
    
    def _add_dependency(self, builder):
        builder.trigger(self)