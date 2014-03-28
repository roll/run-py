from box.functools import cachedproperty
from ..dispatcher import NullDispatcher
from ..settings import settings
from .module import Module

class NullModule(Module):

    #Public
    
    def __meta_init__(self, module):
        super().__meta_init__(self)
        
    def __bool__(self):
        return False
    
    @property
    def meta_basedir(self):
        return self._meta_default_basedir
    
    @cachedproperty
    def meta_dispatcher(self):
        return self._meta_null_dispatcher_class()
    
    @property
    def meta_qualname(self):
        return self.meta_name    
    
    #Protected
    
    _meta_null_dispatcher_class = NullDispatcher
    _meta_default_basedir = settings.default_basedir