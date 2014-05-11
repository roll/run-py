from .method import MethodTask

class task:
    """Make task from method with default kwargs to invoke.
      
    - as function::
      
       task = task(method, **kwargs)      
      
    - as decorator::
      
        @task(**kwargs)
        def method(self):
            pass
    """
    
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
    
    _task_class = MethodTask
    
    @classmethod
    def _make_task(cls, method, **kwargs):
        return cls._task_class(method, **kwargs) 