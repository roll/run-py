from abc import ABCMeta, abstractmethod        

class AttributeUpdate(metaclass=ABCMeta):
    
    #Public
    
    @abstractmethod
    def apply(self, attribute):
        pass #pragma: no cover
            
            
class AttributeSet:
    
    #Public
    
    def __init__(self, name, value):
        self._name = name
        self._value = value
    
    def apply(self, attribute):
        setattr(attribute, self._name, self._value)
        
        
class AttributeCall:
    
    #Public
    
    def __init__(self, name, *args, **kwargs):
        self._name = name
        self._args = args
        self._kwargs = kwargs
        
    def apply(self, attribute):
        method = getattr(attribute, self._name)
        method(*self._args, **self._kwargs)