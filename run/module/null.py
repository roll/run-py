from lib31.python import cachedproperty
from ..dispatcher import NullDispatcher
from ..settings import settings
from .base import BaseModule

class NullModule(BaseModule):

    #Public
    
    def __bool__(self):
        return False
    
    @property
    def meta_basedir(self):
        return self._meta_default_path
    
    @cachedproperty
    def meta_dispatcher(self):
        return self._meta_dispatcher_class()
     
    @property
    def meta_module(self):
        return self
    
    @meta_module.setter
    def meta_module(self, module):
        #TODO: improve message
        raise AttributeError('Cant\'t set attribute')
    
    #Protected
    
    _meta_dispatcher_class = NullDispatcher
    _meta_default_path = settings.default_path