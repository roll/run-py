from abc import ABCMeta, abstractmethod
from lib31.python import cachedproperty
from .property import Property

class Var(Property, metaclass=ABCMeta):
    
    #Public

    def __get__(self, owner, owner_class=None):
        super().__get__(owner, owner_class)
        return self.value
 
    @cachedproperty
    def value(self):
        self._resolve()
        return self.retrieve()
    
    def reset(self):
        cachedproperty.reset(self, 'value')
        
        
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