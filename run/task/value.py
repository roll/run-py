from .task import Task

class ValueTask(Task):
    
    #Public
    
    def __init__(self, value):
        self._value = value
 
    def invoke(self):
        return self._value