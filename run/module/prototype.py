from copy import copy
from ..attribute import AttributePrototype

class ModulePrototype(AttributePrototype):
    
    #Public
    
    def __init__(self, cls, *args, **kwargs):
        super().__init__(copy(cls), *args, **kwargs)
        
    #Protected
    
    _attribute_prototype_class = AttributePrototype
     
    def _create_attribute(self):
        module = super()._create_attribute()
        for key, attr in vars(self._class).items():
            if isinstance(attr, self._attribute_prototype_class):
                    setattr(self._class, key, attr(module))
        return module   
        