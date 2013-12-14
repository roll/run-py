from abc import ABCMeta
from .module import Module
from .task import Task

class Run(Module, metaclass=ABCMeta):
    
    #Public
        
    default = Task(
        require=['help'],
    )