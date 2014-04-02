from abc import ABCMeta
from box.functools import DEFAULT
from .null_module import NullModule
from .prototype import AttributePrototype

class AttributeMetaclass(ABCMeta):
    
    #Public
    
    def __call__(self, *args, **kwargs):
        module = kwargs.pop('meta_module', DEFAULT)
        prototype = self._prototype_class(self, None, *args, **kwargs)
        if module != DEFAULT:
            if module == None:
                module = NullModule()
            return prototype(module)
        else:
            return prototype
        
    #Protected
    
    _prototype_class = AttributePrototype
