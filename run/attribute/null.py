from box.functools import cachedproperty
from ..dispatcher import NullDispatcher
from ..settings import settings

#TODO: finish interface emulation
class NullModule:

    #Public
        
    def __bool__(self):
        return False
    
    @property
    def meta_attributes(self):
        return {}    
    
    @property
    def meta_basedir(self):
        return self._meta_default_basedir
    
    @cachedproperty
    def meta_dispatcher(self):
        return self._meta_null_dispatcher_class()
    
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
        return self._meta_default_main_module_name
    
    @property
    def meta_qualname(self):
        return self.meta_name    
    
    #Protected
    
    _meta_default_basedir = settings.default_basedir    
    _meta_null_dispatcher_class = NullDispatcher
    _meta_default_main_module_name = settings.default_main_module_name