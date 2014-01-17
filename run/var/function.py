import inspect
from .var import Var

class FunctionVar(Var):
    
    #Public

    def __init__(self, function, *args, **kwargs):
        self._function = function
        self._args = args
        self._kwargs = kwargs
    
    def retrieve(self):
        return self._function(*self._args, **self._kwargs)
    
    @property    
    def meta_docstring(self):
        return str(inspect.getdoc(self._function))