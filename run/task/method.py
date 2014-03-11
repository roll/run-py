from .function import FunctionTask

class MethodTask(FunctionTask):
    
    #Public
    
    def __init__(self, method, *args, **kwargs):
        super().__init__(method, *args, **kwargs)
        
    def effective_invoke(self, *args, **kwargs):
        return self._function(self.meta_module, *args, **kwargs)
    
    
class task:
    
    #Public
    
    def __init__(self, *args, **kwargs):
        self._args = args
        self._kwargs = kwargs
        
    def __call__(self, method):
        return MethodTask(method, *self._args, **self._kwargs)