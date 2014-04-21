from box.input import input 
from .function import FunctionTask

class InputTask(FunctionTask):

    #Public
    
    def __init__(self, *args, **kwargs):
        super().__init__(input, *args, **kwargs)    