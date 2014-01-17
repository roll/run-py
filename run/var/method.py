from .function import FunctionVar

class MethodVar(FunctionVar):
    
    #Public
    
    def retrieve(self):
        return self._function(self.meta_module, *self._args, **self._kwargs)