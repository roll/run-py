from copy import copy
from .function import FunctionTask

class MethodTask(FunctionTask):
    
    #Public
    
    def __init__(self, method, *args, **kwargs):
        super().__init__(method, *args, **kwargs)
        
    def invoke(self, *args, **kwargs):
        eargs = copy(self._args)
        eargs = eargs+args
        ekwargs = copy(self._kwargs)
        ekwargs.update(kwargs)
        return self._function(self.meta_module, *eargs, **ekwargs)