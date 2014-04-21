from box.findtools import find_strings 
from .function import FunctionTask

class FindTask(FunctionTask):

    #Public
    
    def __init__(self, *args, **kwargs):
        super().__init__(find_strings, *args, **kwargs)