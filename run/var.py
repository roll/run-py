from abc import ABCMeta, abstractmethod
from .attribute import DependentAttributeMixin
from .unit import Unit

class Var(DependentAttributeMixin,
          Unit, metaclass=ABCMeta):
    
    #Public

    def __get__(self, module, module_class=None):
        super().__get__(module, module_class)
        self.resolve()     
        return self.retrieve()
 
    #Protected
 
    @abstractmethod
    def retrieve(self):
        pass #pragma: no cover
    
        
class ValueVar(Var):
    
    #Public
    
    def __init__(self, value, **kwargs):
        self._value = value
        super().__init__(**kwargs)
 
    #Protected
 
    def retrieve(self):
        return self._value
    

class PropertyVar(Var):
    
    #Public
    
    def __init__(self, prop, **kwargs):
        self._property = prop
        super().__init__(**kwargs)
 
    #Protected
 
    def retrieve(self):
        return self._property.__get__(self.namespace, self.namespace.__class__)  