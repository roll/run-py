import inspect
from .dependent import DependentAttribute

class Task(DependentAttribute):
    
    #Public
    
    def __get__(self, module, module_class=None):
        return self
    
    def __call__(self, *args, **kwargs):
        self._resolve_requirements()
        #TODO: add error handling   
        result = self.complete(*args, **kwargs)
        self._process_triggers()
        return result
    
    def complete(self, *args, **kwargs):
        pass
    

class MethodTask(Task):
    
    #Public

    def __init__(self, method):
        self._method = method
        
    @property
    def __doc__(self):
        return self._method.__doc__
    
    def complete(self, *args, **kwargs):
        return self._method(self.meta_module, *args, **kwargs)
        
    @property
    def meta_signature(self):
        return (super().meta_name+
                str(inspect.signature(self._method)))
    
    @property    
    def meta_docstring(self):
        return str(inspect.getdoc(self._method))      