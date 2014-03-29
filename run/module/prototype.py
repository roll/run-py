from box.functools import cachedproperty
from ..attribute import AttributePrototype, build

class ModulePrototype(AttributePrototype):
        
    #Protected
    
    _attribute_prototype_class = AttributePrototype
     
    def _create_attribute(self):
        return object.__new__(self._builded_class)
    
    @cachedproperty
    def _builded_class(self):
        class_type = type(self._class)
        return class_type(self._builded_class_name, 
                          self._builded_class_bases,
                          self._builded_class_attrs)
    
    @cachedproperty
    def _builded_class_name(self):
        return self._class.__name__+'Builded'
    
    @cachedproperty
    def _builded_class_bases(self):
        return (self._class,)
    
    @cachedproperty
    def _builded_class_attrs(self):
        attrs = {}
        for cls in reversed(self._class.mro()):
            for key, attr in vars(cls).items():
                if isinstance(attr, self._attribute_prototype_class):
                    attrs[key] = build(attr, module=True)
        attrs['__doc__'] = self._class.__doc__
        attrs['__module__'] = self._class.__module__
        return attrs