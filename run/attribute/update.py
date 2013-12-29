from abc import ABCMeta, abstractmethod

class AttributeBuilderUpdate(metaclass=ABCMeta):
    
    #Public
    
    @abstractmethod
    def apply(self, obj):
        pass #pragma: no cover


class AttributeBuilderSet(AttributeBuilderUpdate):
    
    #Public
    
    def __init__(self, name, value):
        self._name = name
        self._value = value
    
    def apply(self, obj):
        setattr(obj, self._name, self._value)
    
    
class AttributeBuilderCall(AttributeBuilderUpdate):
    
    #Public
    
    def __init__(self, name, *args, **kwargs):
        self._name = name
        self._args = args
        self._kwargs = kwargs
        
    def apply(self, obj):
        method = getattr(obj, self._name)
        method(*self._args, **self._kwargs)