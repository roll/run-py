from .module import Module
from .task import Task

#TODO: remove module inheritance?
class Run(Module):
    
    #Public
    
    def __call__(self, attribute_name, *args, **kwargs):
        attribute = getattr(self, attribute_name)
        if callable(attribute):
            result = attribute(*args, **kwargs)
            return result
        else:
            return attribute
        
    default = Task(
        require=['help'],
    )