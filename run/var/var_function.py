from ..task import task
from .descriptor import DescriptorVar

class var(task):
    """Make var from method with default kwargs to invoke.
      
    - as function::
      
       var = var(method, **kwargs)      
      
    - as decorator::
      
        @var(**kwargs)
        def method(self):
            pass
    """    
    
    #Protected
    
    _task_class = DescriptorVar
    
    @classmethod
    def _make_task(cls, method, **kwargs):
        return cls._task_class(property(method), **kwargs)