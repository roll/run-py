import inspect
from abc import ABCMeta, abstractmethod
from copy import copy
from .task import Task

class PartialTask(Task, metaclass=ABCMeta):

    #Public
    
    def __system_prepare__(self, *args, **kwargs):
        self._is_expand = kwargs.pop('is_expand', True)
        super().__system_prepare__(*args, **kwargs)

    def __init__(self, *args, **kwargs):
        self._args = args
        self._kwargs = kwargs
    
    def invoke(self, *args, **kwargs):
        args = self._combine(self._args, args)
        kwargs = self._combine(self._kwargs, kwargs)
        if self._is_expand:
            args = self._expand(args)
            kwargs = self._expand(kwargs)
        return self.effective_invoke(*args, **kwargs) 
    
    @abstractmethod
    def effective_invoke(self, *args, **kwargs):
        pass #pragma: no cover
    
    #Protected
    
    def _combine(self, args1, args2):
        result = copy(args1)
        try:
            result.update(args2)
        except AttributeError:
            result = result+args2
        return result
    
    def _expand(self, args):
        try:
            iterator = args.items()
            result = {}            
        except AttributeError:
            iterator = enumerate(args)
            result = [None]*len(args)            
        for key, value in iterator:
            result[key] = self._expand_value(value)
        result = type(args)(result)
        return result                 
    
    def _expand_value(self, value):
        if inspect.isdatadescriptor(value):
            value = value.__get__(self.meta_module, type(self.meta_module))
        return value