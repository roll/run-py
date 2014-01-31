from ..task import FunctionTask
from .module import Module

class AutoModule(Module):

    #Public

    def __init__(self, *objects):
        self._objects = objects
        for name, function in self._functions.items():
            if not hasattr(type(self), name):
                setattr(type(self), name, FunctionTask(function))
                
    #Protected
    
    @property
    def _functions(self):
        functions = {}
        for obj in reversed(self._objects):
            for name in dir(obj):
                if name.startswith('_'):
                    continue
                value = getattr(obj, name)
                if not callable(value):
                    continue
                if isinstance(value, type):
                    continue
                functions[name] = value
        return functions                   