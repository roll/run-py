from box.intertools import rich_input
from .function import FunctionTask

class InputTask(FunctionTask):

    #Public
    
    def __init__(self, *args, **kwargs):
        super().__init__(rich_input, *args, **kwargs)    