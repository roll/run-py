import logging
from box.functools import cachedproperty
from abc import ABCMeta, abstractmethod

class Resolver(metaclass=ABCMeta):

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
        
        
class CommonResolver(Resolver):

    #Public
    
    def __init__(self, task, *args, **kwargs):
        self._task_name = task
        self._args = args
        self._kwargs = kwargs
        self._enabled = True
        
    def __repr__(self):
        if self._task:
            result = repr(self._task)
            if self._args or self._kwargs:
                result += '('
                elements = []
                for arg in self._args:
                    element = repr(arg)
                    elements.append(element)
                for kwarg in self._kwargs.items():
                    element = '{0}={1}'.format(*kwarg)
                    elements.append(element)
                result += ', '.join(elements)
                result += ')'
            return result
        else:
            return ('<NotExistent "{task_name}">'.
                format(task_name=self._task_name))

    def enable(self, task):
        if task == self._task:
            self._enabled = True
    
    def disable(self, task):
        if task == self._task:
            self._enabled = False
    
    def resolve(self):
        if self._task:
            self._task(*self._args, **self._kwargs)
        
    #Protected
    
    @cachedproperty
    def _task(self):
        if self._attribute:
            from ..task import Task
            module = self._attribute.meta_module
            try:
                from ..module import attribute
                return attribute(module, self._task_name, 
                    category=Task, resolve=True)
            except AttributeError as exception:
                if self._attribute.meta_strict:
                    raise
                else:
                    logger = logging.getLogger(__name__)
                    logger.warning(str(exception))
                    return None
        else:
            raise RuntimeError(
                'Dependency resolver "{resolver}" '
                'is not bound to any attribute'.
                format(resolver=self))
        
        
class NestedResolver(Resolver):

    #Public
    
    def __init__(self, resolvers):
        self._resolvers = resolvers
        
    def __repr__(self):
        elements = []
        for resolver in self._resolvers:
            elements.append(repr(resolver))        
        return repr(elements)        
        
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