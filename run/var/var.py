from abc import ABCMeta
from box.functools import DEFAULT
from ..task import Task
from .signal import InitiatedVarSignal, SuccessedVarSignal

class Var(Task, metaclass=ABCMeta):
    
    #Public
        
    def __build__(self, module, *args, **kwargs):
        self._cached_value = DEFAULT
        super().__build__(module, *args, **kwargs)

    def __get__(self, module, module_class=None):
        if self.meta_cache:
            if self._cached_value == DEFAULT:
                self._cached_value = self()
            return self._cached_value
        else:
            return self()
 
    def __set__(self, module, value):
        self.invoke = lambda: value
        
    @property
    def meta_cache(self):
        """Var's caching status (enabled or disabled).
        
        If meta_cache is True var caches 
        results after first invocation.        
           
        This property is:
        
        - initable/writable
        - inherited from module
        """ 
        return self._meta_params.get('cache', 
            self.meta_module.meta_cache)
    
    @meta_cache.setter
    def meta_cache(self, value):
        self._meta_params['cache'] = value        
    
    @property
    def meta_signature(self):
        return ''
        
    #Protected
    
    _initiated_signal_class = InitiatedVarSignal
    _successed_signal_class = SuccessedVarSignal