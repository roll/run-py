from abc import ABCMeta
from .module import Module
from .task import Task

class Run(Module, metaclass=ABCMeta):
    
    #Public
    
    #TODO: rewrite using NamespaceAttributes 
    def __call__(self, task, *args, **kwargs):
        attribute = getattr(self, task)
        if callable(attribute):
            result = attribute(*args, **kwargs)
            if result:
                print(result)
        else:
            print(attribute)
        
    default = Task(
        require=['help'],
    )