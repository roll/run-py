from .task import Task

class ValueTask(Task):
    
    #Public
 
    def invoke(self, value):
        return value