from ..task import DescriptorTask, task
from .var import Var

class DescriptorVar(Var, DescriptorTask): 
    
    #Public
    
    pass


class var(task):
    
    #Protected
    
    @staticmethod
    def _make_task(method, **kwargs):
        return DescriptorVar(property(method), **kwargs)