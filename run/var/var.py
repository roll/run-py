from abc import ABCMeta
from box.functools import DEFAULT
from ..task import Task
from .signal import InitiatedVarSignal, SuccessedVarSignal

class Var(Task, metaclass=ABCMeta):
    
    #Public
        
    def __meta_init__(self, module, *args, **kwargs):
        self._meta_cache = kwargs.pop('cache', True)
        self._meta_cached = DEFAULT
        super().__meta_init__(module, *args, **kwargs)

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
        """Return caching status (enabled or disabled).
           This property is writable.""" 
        return self._meta_cache
    
    @meta_cache.setter
    def meta_cache(self, value):
        self._meta_cache = value
    
    #Protected
    
    _initiated_signal_class = InitiatedVarSignal
    _successed_signal_class = SuccessedVarSignal