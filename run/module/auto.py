from ..task import FunctionTask
from .module import Module

class AutoModule(Module):

    #Public

    def __init__(self, *objects):
        self._objects = list(objects)+self._default_objects
        for name, function in self._functions.items():
            if not hasattr(type(self), name):
                task = FunctionTask(function, module=self)
                setattr(type(self), name, task)
                
    #Protected
    
    _default_objects = []
    
    @property
    def _functions(self):
        functions = {}
        for obj in reversed(self._objects):
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