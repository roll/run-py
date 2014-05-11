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
        return settings.default_meta_cache
    
    @property
    def meta_chdir(self):
        return settings.default_meta_chdir     
    
    @cachedproperty
    def meta_dispatcher(self):
        return self._dispatcher_class()
    
    @property
    def meta_docstring(self):
        return 'NullModule'
    
    @property
    def meta_fallback(self):
        return settings.default_meta_fallback
    
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
        return settings.default_meta_main_module_name
    
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
    
    _dispatcher_class = NullDispatcher