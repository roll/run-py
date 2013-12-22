from .attribute import AttributeBuilder, AttributeMeta, Attribute
from .wrapper import Wrapper

class ModuleBuilder(AttributeBuilder):
        
    #Protected
       
    def _create_object(self):
        return object.__new__(self._builded_class)
    
    @property
    def _builded_class(self):
        return ModuleMeta(self._builded_class_name, 
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
            for key, attr in cls.__dict__.items():
                if isinstance(attr, AttributeBuilder):
                    dct[key] = attr()
        dct['__module__'] = self._class.__module__
        return dct


class ModuleMeta(AttributeMeta):
     
    #Public
     
    def __new__(cls, name, bases, dct):
        wrapper = Wrapper()
        for key, attr in dct.items():
            if (not key.startswith('_') and
                #TODO: add ignored attributes?
                not key in ['root', 'attributes'] and
                not isinstance(attr, type) and
                not isinstance(attr, Attribute) and
                not isinstance(attr, AttributeBuilder)):
                dct[key] = wrapper.wrap(attr)
        return super().__new__(cls, name, bases, dct)
    
    #Protected
    
    _builder_class = ModuleBuilder 
    
    
class Module(Attribute, metaclass=ModuleMeta):
    
    #Public
    
    def __system_init__(self, args, kwargs):
        super().__system_init__(args, kwargs)
        for attribute in self.attributes.values():
            attribute.module = self
        
    def __get__(self, module, module_class):
        return self
    
    def __getattr__(self, name):
        try:
            module_name, attribute_name = name.split('.', 1)
        except ValueError:
            raise AttributeError(name) from None
        module = getattr(self, module_name)
        attribute = getattr(module, attribute_name)
        return attribute

    @property
    def root(self):
        if self.module:
            return self.module.root
        else:
            return self
        
    @property
    def attributes(self):
        return ModuleAttributes(self)
            
    #Protected
    
    _builder_class = ModuleBuilder
    

class ModuleAttributes(dict):
    
    #Public
    
    def __init__(self, module):
        for name, attr in module.__class__.__dict__.items():
            if isinstance(attr, Attribute):
                self[name] = attr
    
    def find(self, attribute, default=None):
        for name, value in self.items():
            if attribute == value:
                return name
        else:
            return default
        
    def filter(self, attribute_class):
        return {name: value for name, value in self.items() 
                if isinstance(value, attribute_class)}