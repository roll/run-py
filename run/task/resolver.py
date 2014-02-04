from abc import ABCMeta, abstractmethod

class TaskResolver(metaclass=ABCMeta):

    #Public
    
    @abstractmethod
    def enable(self, task):
        pass #pragma: no cover
    
    @abstractmethod
    def disable(self, task):
        pass #pragma: no cover
    
    @abstractmethod    
    def resolve(self, attribute):
        pass #pragma: no cover
        
        
class TaskCommonResolver(TaskResolver):

    #Public
    
    def __init__(self, task, *args, **kwargs):
        self._task = task
        self._args = args
        self._kwargs = kwargs
        self._enabled = True

    def enable(self, task):
        if task == self._task:
            self._enabled = True
    
    def disable(self, task):
        if task == self._task:
            self._enabled = False
    
    def resolve(self, attribute):
        task = getattr(attribute.meta_module, self._task)
        task(*self._args, **self._kwargs)
        
        
class TaskNestedResolver(TaskResolver):

    #Public
    
    def __init__(self, resolvers):
        self._resolvers = resolvers

    def enable(self, task):
        for resolver in self._resolvers:
            resolver.enable(task)
    
    def disable(self, task):
        for resolver in self._resolvers:
            resolver.disable(task)
    
    def resolve(self, attribute):
        for resolver in self._resolvers:
            resolver.resolve(attribute)