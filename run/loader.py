import inspect
from lib31.python import ObjectLoader
from .module import Module
    
class ModuleLoader(ObjectLoader):
    
    #Public
    
    def load(self, base_dir, file_pattern):
        modules = []
        objects = super().load(base_dir, file_pattern)
        for obj in objects:
            if (isinstance(obj, type) and
                issubclass(obj, Module) and
                not inspect.isabstract(obj)):
                modules.append(obj)
        return modules