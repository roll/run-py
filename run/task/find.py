from box.findtools import find_strings 
from .task import Task

class FindTask(Task):

    #Public
        
    def invoke(self, *args, **kwargs):
        return find_strings(*args, **kwargs)