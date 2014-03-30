from abc import ABCMeta
from .prototype import AttributePrototype

class AttributeMetaclass(ABCMeta):
    
    #Public
    
    def __call__(self, *args, **kwargs):
        build = kwargs.pop('build', False)
        prototype = self._prototype_class(self, *args, **kwargs)
        if build:
            return prototype()
        else:
            return prototype
        
    #Protected
    
    _prototype_class = AttributePrototype
