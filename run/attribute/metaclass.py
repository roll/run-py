from abc import ABCMeta
from box.functools import DEFAULT
from .prototype import AttributePrototype

class AttributeMetaclass(ABCMeta):
    
    #Public
    
    def __call__(self, *args, **kwargs):
        module = kwargs.pop('module', DEFAULT)
        prototype = self._prototype_class(self, None, *args, **kwargs)
        if module != DEFAULT:
            return prototype(module)
        else:
            return prototype
        
    #Protected
    
    _prototype_class = AttributePrototype
