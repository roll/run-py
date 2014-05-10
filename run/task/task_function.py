from .method import MethodTask

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