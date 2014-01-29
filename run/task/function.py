import inspect
from copy import copy
from .task import Task

class FunctionTask(Task):
    
    #Public

    def __init__(self, function, *args, **kwargs):
        self._function = function
        self._args = args
        self._kwargs = kwargs
    
    def invoke(self, *args, **kwargs):
        eargs = copy(self._args)
        eargs = eargs+args
        ekwargs = copy(self._kwargs)
        ekwargs.update(kwargs)
        return self._function(*eargs, **ekwargs)
        
    @property
    def meta_signature(self):
        return (self.meta_qualname+
                str(inspect.signature(self._function)))
    
    @property    
    def meta_docstring(self):
        return str(inspect.getdoc(self._function))