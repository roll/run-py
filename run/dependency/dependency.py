from abc import ABCMeta, abstractmethod
from box.functools import cachedproperty
from .resolver import (Resolver, CommonResolver, 
                       NestedResolver)

class Dependency(Resolver, metaclass=ABCMeta):
    
    #Public
    
    def __init__(self, task, *args, **kwargs):
        self._task = task
        self._args = args
        self._kwargs = kwargs
        self._is_resolved = False
        
    def __repr__(self):
        return '{category} {resolver}'.format(
            category=type(self).__name__,
            resolver=repr(self._resolver))        
    
    def bind(self, attribute):
        self._resolver.bind(attribute)
    
    def enable(self, task):
        self._resolver.enable(task)
    
    def disable(self, task):
        self._resolver.disable(task)
     
    @abstractmethod    
    def resolve(self, failed=None):
        pass #pragma: no cover

    @property
    def is_resolved(self):
        return self._is_resolved
    
    #Protected
    
    @cachedproperty
    def _resolver(self):
        if not isinstance(self._task, list):
            resolver = CommonResolver(
                self._task, *self._args, **self._kwargs)
        else:
            dependencies = []
            for dependency in self._task:
                if not isinstance(self._task, type(self)):
                    dependency = type(self)(
                        dependency, *self._args, **self._kwargs)
                dependencies.append(dependency)
            resolver = NestedResolver(dependencies)
        return resolver