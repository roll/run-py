import inspect
from .var import Var

class DescriptorVar(Var):
    
    #Public
    
    def __init__(self, descriptor):
        self._descriptor = descriptor
 
    def retrieve(self):
        return self._descriptor.__get__(
            self.meta_module, type(self.meta_module))
    
    @property    
    def meta_docstring(self):
        return str(inspect.getdoc(self._descriptor))