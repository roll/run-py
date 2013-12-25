import inspect
from lib31.python import ObjectLoader
from .module import Module
    
class ModuleLoader(ObjectLoader):
    
    #Public
    
    def load(self, base_dir, file_pattern):
        objects = super().load(base_dir, file_pattern)
        modules = []
        for obj in objects:
            if (isinstance(obj, type) and
                issubclass(obj, Module) and
                not inspect.isabstract(obj)):
                modules.append(obj)
        return modules
    
    #Protected
    
    def _filter_object(self, obj, module, name):
        if not super()._filter_object(obj, module, name):
            return False
        elif inspect.getmodule(obj) != module:
            return False
        else:
            return True