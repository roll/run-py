import re
from .function import FunctionTask

class MethodTask(FunctionTask):
    
    #Public
    
    def __init__(self, method, *args, **kwargs):
        super().__init__(method, *args, **kwargs)
        
    @property
    def meta_signature(self):
        return self._meta_params.get('signature', 
            re.sub('self[,\s]*', '', super().meta_signature))        
        
    def invoke(self, *args, **kwargs):
        return self._function(self.meta_module, *args, **kwargs)
    
    
class task:
    
    #Public
    
    def __new__(cls, *args, **kwargs):
        if args:
            return cls._make_task(args[0], **kwargs)
        else:
            return super().__new__(cls)
    
    def __init__(self, **kwargs):
        self._kwargs = kwargs
        
    def __call__(self, method):
        return self._make_task(method, **self._kwargs)
    
    #Protected
    
    @staticmethod
    def _make_task(method, **kwargs):
        return MethodTask(method, **kwargs)
    
    
def skip(method):
    setattr(method, '__isskippedmethod__', True)
    return method    