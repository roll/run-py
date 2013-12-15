from abc import ABCMeta, abstractmethod
from .attribute import DependentAttributeMixin

class Var(DependentAttributeMixin,
          metaclass=ABCMeta):
    
    #Public

    def __get__(self, module, module_class=None):
        super().__get__(module, module_class)
        self._resolve()     
        return self._retrieve()
 
    #Protected
 
    @abstractmethod
    def _retrieve(self):
        pass #pragma: no cover
    
        
class ValueVar(Var):
    
    #Public
    
    def __init__(self, value, **kwargs):
        self._value = value
        super().__init__(**kwargs)
 
    #Protected
 
    def _retrieve(self):
        return self._value
    

class PropertyVar(Var):
    
    #Public
    
    def __init__(self, prop, **kwargs):
        self._property = prop
        super().__init__(**kwargs)
 
    #Protected
 
    def _retrieve(self):
        return self._property.__get__(self._namespace, self._namespace.__class__)  