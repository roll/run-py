from box.functools import Function
from ..task import FunctionTask
from .module import Module

class AutoModule(Module):

    #Public

    def __init__(self, sources=[]):
        self._sources = sources+self._default_sources
        for task_name, task_function in self._functions.items():
            if not hasattr(type(self), task_name):
                task = FunctionTask(task_function, meta_module=self)
                setattr(type(self), task_name, task)
   
    @property             
    def meta_docstring(self):
        if self._meta_docstring != None:
            return self._meta_docstring
        else:
            return ('AutoModule with following sources: {sources}'.
                    format(sources=self._sources))
                
    #Protected
    
    _default_sources = []
    
    @property
    def _functions(self):
        functions = {}
        for obj in reversed(self._sources):
            for name in dir(obj):
                if name.startswith('_'):
                    continue
                attr = getattr(obj, name)
                if not callable(attr):
                    continue
                if isinstance(attr, type):
                    if not isinstance(attr, Function):
                        continue
                functions[name] = attr
        return functions                   