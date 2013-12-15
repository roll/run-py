from abc import ABCMeta
from .module import Module
from .task import Task

class Run(Module, metaclass=ABCMeta):
    
    #Public
    
    #TODO: rewrite using NamespaceAttributes 
    def __call__(self, attribute_name, *args, **kwargs):
        attribute = getattr(self, attribute_name)
        if callable(attribute):
            result = attribute(*args, **kwargs)
            return result
        else:
            return result
        
    default = Task(
        require=['help'],
    )