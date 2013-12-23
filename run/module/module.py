__all__ = ['ModuleMeta', 'Module']

from ..attribute import AttributeBuilder, AttributeMeta, Attribute
from ..wrapper import Wrapper
from .attributes import ModuleAttributes
from .builder import ModuleBuilder

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