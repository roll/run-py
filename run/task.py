import inspect
from .attribute import DependentAttribute, AttributeMetadata

class Task(DependentAttribute):
    
    #Public
    
    def __get__(self, module, module_class=None):
        return self
    
    def __call__(self, *args, **kwargs):
        self.resolve_requirements()        
        result = self.complete(*args, **kwargs)
        self.process_triggers()
        return result
    
    def complete(self, *args, **kwargs):
        pass


class MethodTask(Task):
    
    #Public

    def __init__(self, method, **kwargs):
        super().__init__(**kwargs)
        self._method = method
        
    @property
    def __doc__(self):
        return self._method.__doc__
    
    def complete(self, *args, **kwargs):
        return self._method(self.module, *args, **kwargs)
        
    @property    
    def metadata(self):
        return AttributeMetadata(
            self, signature=self._signature, 
                  docstring=self._docstring)
        
    #Protected
    
    @property
    def _signature(self):
        return (super().metadata.name+
                str(inspect.signature(self._method)))
    
    @property    
    def _docstring(self):
        return str(inspect.getdoc(self._method))                                 