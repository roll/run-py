import inspect
from .task import Task

#TODO: rename to FunctionTask?
class MethodTask(Task):
    
    #Public

    def __init__(self, method):
        self._method = method
    
    def complete(self, *args, **kwargs):
        return self._method(self.meta_module, *args, **kwargs)
        
    @property
    def meta_signature(self):
        return (self.meta_qualname+
                str(inspect.signature(self._method)))
    
    @property    
    def meta_docstring(self):
        return str(inspect.getdoc(self._method))   