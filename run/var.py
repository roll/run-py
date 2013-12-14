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
        super().__init__(**kwargs)
        self._value = value
 
    def retrieve(self):
        return self._value
    

class DescriptorVar(Var):
    
    def __init__(self, descriptor, **kwargs):
        super().__init__(**kwargs)
        self._descriptor = descriptor
 
    def retrieve(self):
        return self._descriptor(self._run, self._run.__class__)  