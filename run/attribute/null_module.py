from box.functools import cachedproperty
from ..dispatcher import NullDispatcher
from ..settings import settings

class NullModule:

    #Public
        
    def __bool__(self):
        return False
    
    @property
    def meta_attributes(self):
        return {}    
    
    @property
    def meta_basedir(self):
        return self._default_basedir
    
    @property
    def meta_cache(self):
        return None
    
    @property
    def meta_chdir(self):
        return None      
    
    @cachedproperty
    def meta_dispatcher(self):
        return self._null_dispatcher_class()
    
    @property
    def meta_docstring(self):
        return ''
    
    @property
    def meta_fallback(self):
        return None
    
    @property
    def meta_is_main_module(self):
        return True
    
    @property
    def meta_info(self):
        return self.meta_signature  
    
    @property
    def meta_main_module(self):
        return self    
    
    @property
    def meta_module(self):
        return self
    
    @property
    def meta_name(self):
        return self._default_main_module_name
    
    @property
    def meta_qualname(self):
        return self.meta_name
    
    @property
    def meta_signature(self):
        return self.meta_qualname
    
    @property
    def meta_tags(self):
        return []    
    
    @property
    def meta_type(self):
        return type(self).__name__    
    
    #Protected
    
    _default_basedir = settings.default_basedir    
    _null_dispatcher_class = NullDispatcher
    _default_main_module_name = settings.default_main_module_name