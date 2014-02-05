from abc import ABCMeta
from box.functools import DEFAULT
from ..task import Task
from .signal import InitiatedVarSignal, ProcessedVarSignal

class Var(Task, metaclass=ABCMeta):
    
    #Public
    
    def __system_prepare__(self, *args, **kwargs):
        self._is_cache = kwargs.pop('is_cache', True)
        super().__system_prepare__(*args, **kwargs)
        
    def __system_init__(self):
        self._cache = DEFAULT        
        super().__system_init__()        

    def __get__(self, module, module_class=None):
        if self._is_cache:
            if self._cache == DEFAULT:
                self._cache = self()
            return self._cache
        return self()
 
    def __set__(self, module, value):
        self.invoke = lambda: value
    
    #Protected
    
    _initiated_signal_class = InitiatedVarSignal
    _processed_signal_class = ProcessedVarSignal