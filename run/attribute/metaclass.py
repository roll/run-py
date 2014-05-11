from abc import ABCMeta
from box.functools import DEFAULT
from .prototype import AttributePrototype

class AttributeMetaclass(ABCMeta):
    
    #Public
    
    def __call__(self, *args, **kwargs):
        module = kwargs.pop('meta_module', DEFAULT)
        prototype = self._prototype_class(self, None, *args, **kwargs)
        if module != DEFAULT:
            if module == None:
                from ..module import NullModule
                module = NullModule()
            return prototype.__build__(module)
        else:
            return prototype
        
    #Protected
    
    _prototype_class = AttributePrototype
