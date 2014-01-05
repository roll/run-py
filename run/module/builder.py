from lib31.python import cachedproperty
from ..attribute import AttributeBuilder

class ModuleBuilder(AttributeBuilder):
        
    #Protected
    
    _attribute_builder_class = AttributeBuilder
     
    #TODO: add no builded class (use effective_class) if no Attributes?   
    def _create_object(self):
        return object.__new__(self._builded_class)
    
    @cachedproperty
    def _builded_class(self):
        class_type = type(self._class)
        return class_type(self._builded_class_name, 
                          self._builded_class_bases,
                          self._builded_class_dict)
    
    @cachedproperty
    def _builded_class_name(self):
        return self._class.__name__+'Builded'
    
    @cachedproperty
    def _builded_class_bases(self):
        return (self._class,)
    
    @cachedproperty
    def _builded_class_dict(self):
        dct = {}
        for cls in reversed(self._class.mro()):
            for key, attr in vars(cls).items():
                if isinstance(attr, self._attribute_builder_class):
                    dct[key] = attr()
        dct['__doc__'] = self._class.__doc__
        dct['__module__'] = self._class.__module__
        return dct