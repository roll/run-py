from copy import copy
from ..attribute import AttributePrototype

class ModulePrototype(AttributePrototype):
    
    #Public
    
    def __init__(self, cls, updates, *args, **kwargs):
        super().__init__(copy(cls), updates, *args, **kwargs)
        
    #Protected
    
    _attribute_prototype_class = AttributePrototype
     
    def _create_attribute(self):
        module = super()._create_attribute()
        for name in dir(self._class):
            attr = getattr(self._class, name)
            if isinstance(attr, self._attribute_prototype_class):
                setattr(self._class, name, attr.__build__(module))
        return module    