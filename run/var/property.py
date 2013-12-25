import inspect
from .var import Var

class PropertyVar(Var):
    
    #Public
    
    def __init__(self, prop):
        self._property = prop
 
    def retrieve(self):
        return self._property.__get__(
            self.meta_module, self.meta_module.__class__)
    
    @property    
    def meta_docstring(self):
        return str(inspect.getdoc(self._property))  