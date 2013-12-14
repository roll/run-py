from .module import Module
from .task import Task

class Run(Module):
    
    #Public
        
    default = Task(
        require=['help'],
    )