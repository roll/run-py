from abc import ABCMeta
from box.functools import DEFAULT
from ..task import Task
from .signal import InitiatedVarSignal, ProcessedVarSignal

class Var(Task, metaclass=ABCMeta):
    
    #Public
        
    def __system_init__(self):
        super().__system_init__()
        kwargs = self.__system_kwargs__
        self._is_cache = kwargs.pop('is_cache', True)
        self._cache = DEFAULT

    def __get__(self, module, module_class=None):
        if self._is_cache:
            if self._cache == DEFAULT:
                self._cache = self()
            return self._cache
        return self()
 
    def __set__(self, module, value):
        self.invoke = lambda: value
    
    @property    
    def meta_is_cache(self):
        return self._is_cache
    
    #Protected
    
    _initiated_signal_class = InitiatedVarSignal
    _processed_signal_class = ProcessedVarSignal