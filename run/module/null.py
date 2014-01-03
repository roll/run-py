from lib31.python import cachedproperty
from ..dispatcher import NullDispatcher
from ..settings import settings
from .base import BaseModule

class NullModule(BaseModule):

    #Public
    
    def __bool__(self):
        return False
        
    @property
    def meta_module(self):
        return None
    
    @cachedproperty
    def meta_dispatcher(self):
        return NullDispatcher()
    
    @property
    def meta_basedir(self):
        return settings.default_path
    
    @property
    def meta_name(self):
        return ''    