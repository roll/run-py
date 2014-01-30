import inspect
from .partial import PartialTask

class FunctionTask(PartialTask):
    
    #Public

    def __init__(self, function, *args, **kwargs):
        self._function = function
        super().__init__(*args, **kwargs)
    
    def effective_invoke(self, *args, **kwargs):
        return self._function(*args, **kwargs)
        
    @property
    def meta_signature(self):
        return (self.meta_qualname+
                str(inspect.signature(self._function)))
    
    @property    
    def meta_docstring(self):
        return str(inspect.getdoc(self._function))