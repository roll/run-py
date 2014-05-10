from ..task import task
from .descriptor import DescriptorVar

class var(task):
    
    #Protected
    
    @staticmethod
    def _make_task(method, **kwargs):
        return DescriptorVar(property(method), **kwargs)