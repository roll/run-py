from abc import ABCMeta
from .prototype import AttributePrototype, build

class AttributeMetaclass(ABCMeta):
    
    #Public
    
    def __call__(self, *args, **kwargs):
        build = kwargs.pop('build', False)
        prototype = self._prototype_class(self, *args, **kwargs)
        if build:
            return self._build_function(prototype)
        else:
            return prototype
        
    #Protected
    
    _prototype_class = AttributePrototype
    _build_function = staticmethod(build)