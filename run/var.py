from abc import ABCMeta, abstractmethod
from .attribute import DependentAttributeMixin

class Var(DependentAttributeMixin,
          metaclass=ABCMeta):
    
    #Public

    def __get__(self, module, module_class=None):
        super().__get__(module, module_class)
        self.resolve()     
        return self.retrieve()
 
    @abstractmethod
    def retrieve(self):
        pass #pragma: no cover
    
        
class PlainVar(Var):
    
    def __init__(self, value, **kwargs):
        self._value = value
        super().__init__(**kwargs)
 
    def retrieve(self):
        return self._value
    

class PropertyVar(Var):
    
    def __init__(self, property, **kwargs):
        self._property = property
        super().__init__(**kwargs)
 
    def retrieve(self):
        return self._property(self._run, self._run.__class__)  