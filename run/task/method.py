from .function import FunctionTask

class MethodTask(FunctionTask):
    
    #Public
    
    def __init__(self, method, *args, **kwargs):
        super().__init__(method, *args, **kwargs)
        
    def effective_invoke(self, *args, **kwargs):
        return self._function(self.meta_module, *args, **kwargs)
    
    
class task:
    
    #Public
    
    def __new__(cls, *args, **kwargs):
        if args:
            return MethodTask(args[0], **kwargs)
        else:
            return super().__new__(cls)
    
    def __init__(self, **kwargs):
        self._kwargs = kwargs
        
    def __call__(self, method):
        return MethodTask(method, **self._kwargs)