from abc import ABCMeta, abstractmethod
from .builder import TaskBuilder
from .resolver import TaskResolver, TaskCommonResolver, TaskNestedResolver

class TaskDependency(TaskResolver, metaclass=ABCMeta):
    
    #Public
    
    def __init__(self, task, *args, **kwargs):
        if not isinstance(task, list):
            self._resolver = TaskCommonResolver(task, *args, **kwargs)
        else:
            dependencies = []
            for dependency in task:
                if not isinstance(task, type(self)):
                    dependency = type(self)(dependency, *args, **kwargs)
                    dependencies.append(dependency)
            self._resolver = TaskNestedResolver(dependencies)
        self._resolves = 0
    
    def __call__(self, method):
        if not isinstance(method, self._builder_class):
            builder = self._method_task_class(method)
        else:
            builder = method
        self._add_dependency(builder)
        return builder
    
    def enable(self, task):
        self._resolver.enable(task)
    
    def disable(self, task):
        self._resolver.disable(task)
        
    def resolve(self, attribute):
        self._resolver.resolve(attribute)
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