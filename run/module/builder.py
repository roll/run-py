from ..attribute import AttributeBuilder

class ModuleBuilder(AttributeBuilder):
        
    #Protected
       
    def _create_object(self):
        return object.__new__(self._builded_class)
    
    @property
    def _builded_class(self):
        class_type = type(self._class)
        return class_type(self._builded_class_name, 
                          self._builded_class_bases,
                          self._builded_class_dict)
    
    @property
    def _builded_class_name(self):
        return self._class.__name__+'Builded'
    
    @property
    def _builded_class_bases(self):
        return (self._class,)
    
    @property
    def _builded_class_dict(self):
        dct = {}
        for cls in reversed(self._class.mro()):
            for key, attr in vars(cls).items():
                if isinstance(attr, AttributeBuilder):
                    dct[key] = attr()
        #TODO: check attributes to copy (less/more)
        dct['__doc__'] = self._class.__doc__
        dct['__module__'] = self._class.__module__
        return dct