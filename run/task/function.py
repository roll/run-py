import inspect
from .task import Task

class FunctionTask(Task):
    
    #Public

    def __init__(self, function, *args, **kwargs):
        self._function = function
        super().__init__(*args, **kwargs)
    
    @property    
    def meta_docstring(self):
        return self._meta_params.get('docstring', 
            inspect.getdoc(self._function).strip())
        
    @property
    def meta_signature(self):
        return self._meta_params.get('signature', 
            self.meta_qualname+str(inspect.signature(self._function)))
    
    def invoke(self, *args, **kwargs):
        return self._function(*args, **kwargs)        