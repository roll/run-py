from ..task import DescriptorTask, task
from .var import Var

class DescriptorVar(Var, DescriptorTask): 
    
    #Public
    
    pass


class var(task):
    
    #Protected
    
    @staticmethod
    def _make_task(method, **kwargs):
        if kwargs.get('expand', True):
            descriptor = property(lambda *args, **kwargs: property(method))
        else:
            descriptor = property(method)
        return DescriptorVar(descriptor, **kwargs)