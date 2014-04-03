from box.input import input 
from .task import Task

class InputTask(Task):

    #Public
        
    def invoke(self, *args, **kwargs):
        return input(*args, **kwargs)