from abc import ABCMeta, abstractmethod

class TaskResolver(metaclass=ABCMeta):

    #Public
    
    def bind(self, attribute):
        self._attribute = attribute 
        
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
        self._task_name = task
        self._args = args
        self._kwargs = kwargs
        self._enabled = True

    def enable(self, task):
        if task == self._task:
            self._enabled = True
    
    def disable(self, task):
        if task == self._task:
            self._enabled = False
    
    def resolve(self):
        self._task(*self._args, **self._kwargs)
        
    #Protected
    
    @property
    def _task(self):
        if self._attribute:
            return getattr(
                self._attribute.meta_module, self._task_name)
        else:
            raise RuntimeError(
                'Dependency resolver "{resolver}" is unbound'.
                format(resolver=self))
        
        
class TaskNestedResolver(TaskResolver):

    #Public
    
    def __init__(self, resolvers):
        self._resolvers = resolvers
        
    def bind(self, attribute):
        for resolver in self._resolvers:
            resolver.bind(attribute)       

    def enable(self, task):
        for resolver in self._resolvers:
            resolver.enable(task)
    
    def disable(self, task):
        for resolver in self._resolvers:
            resolver.disable(task)
    
    def resolve(self):
        for resolver in self._resolvers:
            resolver.resolve()