from box.python import cachedproperty
from ..dispatcher import NullDispatcher
from ..settings import settings
from .base import BaseModule

class NullModule(BaseModule):

    #Public
    
    def __bool__(self):
        return False
    
    @property
    def meta_basedir(self):
        return self._meta_default_basedir
    
    @cachedproperty
    def meta_dispatcher(self):
        return self._meta_null_dispatcher_class()
     
    @property
    def meta_module(self):
        return self
    
    @meta_module.setter
    def meta_module(self, module):
        raise AttributeError(
            'Can\'t set meta_module in NullModule')
    
    @property
    def meta_qualname(self):
        return self.meta_name    
    
    #Protected
    
    _meta_null_dispatcher_class = NullDispatcher
    _meta_default_basedir = settings.default_basedir