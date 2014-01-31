from ..task import FunctionTask
from .module import Module

class AutoModule(Module):

    #Public

    def __init__(self, *objects):
        self._meta_objects = objects
        for name, function in self._meta_functions.items():
            if not hasattr(type(self), name):
                setattr(type(self), name, FunctionTask(function))
                
    #Protected
    
    @property
    def _meta_functions(self):
        functions = {}
        for obj in reversed(self._meta_objects):
            for name in dir(obj):
                if name.startswith('_'):
                    continue
                attr = getattr(obj, name)
                if not callable(attr):
                    continue
                if isinstance(attr, type):
                    continue
                functions[name] = attr
        return functions                   