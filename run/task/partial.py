from abc import ABCMeta, abstractmethod
from copy import copy
from .task import Task

class PartialTask(Task, metaclass=ABCMeta):

    #Public

    def __init__(self, *args, is_expand=True, **kwargs):
        self._args = args
        self._is_expand = is_expand
        self._kwargs = kwargs
    
    def invoke(self, *args, **kwargs):
        eargs = self._args+args
        ekwargs = copy(self._kwargs)
        ekwargs.update(kwargs)
        return self.effective_invoke(*eargs, **ekwargs) 
    
    @abstractmethod
    def effective_invoke(self, *args, **kwargs):
        pass #pragma: no cover