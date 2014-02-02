from abc import ABCMeta, abstractmethod

class DependencyResolver(metaclass=ABCMeta):

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
        
        
class DependencyTaskResolver(metaclass=ABCMeta):

    #Public
    
    def __init__(self, task, *args, **kwargs):
        self._task = task
        self._args = args
        self._kwargs = kwargs
        self._enabled = True 

    def enable(self, task):
        self._enabled = True
    
    def disable(self, task):
        self._enabled = False
    
    def resolve(self, attribute):
        task = getattr(attribute.meta_module, self._task)
        task(*self._args, **self._kwargs)
        
        
class DependencyNestedResolver(metaclass=ABCMeta):

    #Public
    
    def __init__(self, dependencies):
        self._dependencies = dependencies

    @abstractmethod
    def enable(self, task):
        for dependency in self._dependencies:
            dependency.enable(task)
    
    @abstractmethod
    def disable(self, task):
        for dependency in self._dependencies:
            dependency.disable(task)
    
    @abstractmethod    
    def resolve(self, attribute):
        for dependency in self._dependencies:
            dependency.resolve(attribute)