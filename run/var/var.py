from abc import ABCMeta
from box.functools import DEFAULT
from ..task import Task
from .signal import InitiatedVarSignal, ProcessedVarSignal

class Var(Task, metaclass=ABCMeta):
    
    #Public
        
    def __meta_init__(self):
        super().__meta_init__()
        kwargs = self._meta_kwargs
        self._meta_is_cache = kwargs.pop('is_cache', True)
        self._meta_cache = DEFAULT

    def __get__(self, module, module_class=None):
        if self.meta_is_cache:
            if self._meta_cache == DEFAULT:
                self._meta_cache = self()
            return self._meta_cache
        return self()
 
    def __set__(self, module, value):
        self.invoke = lambda: value
    
    @property    
    def meta_is_cache(self):
        return self._meta_is_cache
    
    #Protected
    
    _meta_initiated_signal_class = InitiatedVarSignal
    _meta_processed_signal_class = ProcessedVarSignal