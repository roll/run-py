from abc import ABCMeta, abstractmethod
from box.functools import cachedproperty
from .builder import TaskBuilder
from .resolver import TaskResolver, TaskCommonResolver, TaskNestedResolver

class TaskDependency(TaskResolver, metaclass=ABCMeta):
    
    #Public
    
    def __init__(self, task, *args, **kwargs):
        self._task = task
        self._args = args
        self._kwargs = kwargs
        self._is_resolved = False
    
    def __call__(self, method):
        if not isinstance(method, self._builder_class):
            builder = self._method_task_class(method)
        else:
            builder = method
        self._add_dependency(builder)
        return builder
    
    def bind(self, module):
        self._resolver.bind(module)    
    
    def enable(self, task):
        self._resolver.enable(task)
    
    def disable(self, task):
        self._resolver.disable(task)
     
    @abstractmethod    
    def resolve(self, after=False):
        pass #pragma: no cover

    @property
    def is_resolved(self):
        return self._is_resolved
    
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
    
    @cachedproperty
    def _resolver(self):
        if not isinstance(self._task, list):
            resolver = TaskCommonResolver(
                self._task, *self._args, **self._kwargs)
        else:
            dependencies = []
            for dependency in self._task:
                if not isinstance(self._task, type(self)):
                    dependency = type(self)(
                        dependency, *self._args, **self._kwargs)
                dependencies.append(dependency)
            resolver = TaskNestedResolver(dependencies)
        return resolver
               

class require(TaskDependency):
    
    #Public
     
    def resolve(self, after=False):
        if not after:
            if not self._is_resolved:
                self._resolver.resolve()
                self._is_resolved = True
    
    #Protected
    
    def _add_dependency(self, builder):
        builder.require(self)
        
        
class trigger(TaskDependency):
    
    #Public
     
    def resolve(self, after=False):
        if after:
            self._resolver.resolve()
    
    #Protected
    
    def _add_dependency(self, builder):
        builder.trigger(self)                 