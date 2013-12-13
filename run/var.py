from abc import ABCMeta, abstractmethod
from .field import Field

class Var(Field, metaclass=ABCMeta):
    
    #Public

    def __get__(self, owner, owner_class=None):
        super().__get__(owner, owner_class)
        self._manager.resolve()        
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