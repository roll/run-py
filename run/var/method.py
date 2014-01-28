from .function import FunctionVar

class MethodVar(FunctionVar):
    
    #Public
    
    def __init__(self, method, *args, **kwargs):
        super().__init__(method, *args, **kwargs)   
    
    def invoke(self):
        return self._function(self.meta_module, *self._args, **self._kwargs)