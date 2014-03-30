from copy import copy
from ..attribute import AttributePrototype, build

class ModulePrototype(AttributePrototype):
    
    #Public
    
    def __init__(self, cls, *args, **kwargs):
        super().__init__(copy(cls), *args, **kwargs)
        
    #Protected
    
    _attribute_prototype_class = AttributePrototype
     
    def _create_attribute(self):
        cls = copy(self._class)
        for key, attr in vars(cls).items():
            if isinstance(attr, self._attribute_prototype_class):
                    setattr(cls, key, build(attr, module=True))
        return object.__new__(cls)