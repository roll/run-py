from .task import Task

class ValueTask(Task):
    
    #Public
 
    @property    
    def meta_docstring(self):
        return self._meta_params.get('docstring', 
            'Return given value.') 
 
    def invoke(self, value):
        return value