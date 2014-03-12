from abc import ABCMeta
from box.functools import DEFAULT
from ..task import Task
from .signal import InitiatedVarSignal, SuccessedVarSignal

class Var(Task, metaclass=ABCMeta):
    
    #Public
        
    def __meta_init__(self):
        kwargs = self._meta_kwargs
        self._meta_cache = kwargs.pop('cache', True)
        self._meta_cached = DEFAULT
        super().__meta_init__()

    def __get__(self, module, module_class=None):
        if self.meta_cache:
            if self._meta_cached == DEFAULT:
                self._meta_cached = self()
            return self._meta_cached
        return self()
 
    def __set__(self, module, value):
        self.invoke = lambda: value
    
    @property    
    def meta_cache(self):
        return self._meta_cache
    
    #Protected
    
    _meta_initiated_signal_class = InitiatedVarSignal
    _meta_successed_signal_class = SuccessedVarSignal