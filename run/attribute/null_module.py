import os
from box.functools import cachedproperty
from ..dispatcher import NullDispatcher
from ..settings import settings

class NullModule:

    #Public
    
    def __bool__(self):
        return False
    
    def __repr__(self):
        return '<NullModule>'    
    
    @property
    def meta_attributes(self):
        return {}    
    
    @property
    def meta_basedir(self):
        return os.getcwd()
    
    @property
    def meta_cache(self):
        return self._default_meta_cache
    
    @property
    def meta_chdir(self):
        return self._default_meta_chdir     
    
    @cachedproperty
    def meta_dispatcher(self):
        return self._null_dispatcher_class()
    
    @property
    def meta_docstring(self):
        return 'NullModule'
    
    @property
    def meta_fallback(self):
        return self._default_meta_fallback
    
    @property
    def meta_is_main_module(self):
        return True
    
    @property
    def meta_main_module(self):
        return self    
    
    @property
    def meta_module(self):
        return self
    
    @property
    def meta_name(self):
        return self._default_meta_main_module_name
    
    @property
    def meta_qualname(self):
        return self.meta_name
    
    @property
    def meta_tags(self):
        return []    
    
    @property
    def meta_type(self):
        return type(self).__name__    
    
    #Protected
    
    _null_dispatcher_class = NullDispatcher
    _default_meta_cache = settings.default_meta_cache
    _default_meta_chdir  = settings.default_meta_chdir 
    _default_meta_fallback = settings.default_meta_fallback
    _default_meta_main_module_name = settings.default_meta_main_module_name