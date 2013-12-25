import inspect
from lib31.python import ObjectLoader
from .module import Module
    
class ModuleLoader(ObjectLoader):
    
    #Public
    
    def __init__(self, filters=[]):
        self._filters = filters
    
    #Protected
    
    def _filter_object(self, obj, module, name):
        if not super()._filter_object(obj, module, name):
            return False
        if (inspect.getmodule(obj) != module or
              not isinstance(obj, type) or
              not issubclass(obj, Module) or
              inspect.isabstract(obj)):
            return False
        return True