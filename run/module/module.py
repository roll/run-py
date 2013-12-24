from ..attribute import AttributeBuilder, AttributeMetaclass, Attribute
from ..settings import settings
from ..wrapper import Wrapper
from .attributes import ModuleAttributes
from .builder import ModuleBuilder

class ModuleMetaclass(AttributeMetaclass):
     
    #Public
     
    def __new__(cls, name, bases, dct):
        wrapper = Wrapper()
        for key, attr in dct.items():
            if (not key.startswith('_') and
                not key.startswith('meta_') and
                not isinstance(attr, type) and
                not isinstance(attr, Attribute) and
                not isinstance(attr, AttributeBuilder)):
                dct[key] = wrapper.wrap(attr)
        return super().__new__(cls, name, bases, dct)
    
    #Protected
    
    _builder_class = ModuleBuilder
    

class Module(Attribute, metaclass=ModuleMetaclass):
    
    #Public
    
    def __meta_init__(self, args, kwargs):
        super().__meta_init__(args, kwargs)
        for attribute in self.meta_attributes.values():
            attribute.meta_module = self
        
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
    
    def __call__(self, attribute, *args, **kwargs):
        if not attribute:
            #TODO: use settings?
            attribute = settings.default_attribute
        attribute = getattr(self, attribute)
        if callable(attribute):
            result = attribute(*args, **kwargs)
            return result
        else:
            return attribute
    
    #TODO: implement
    @property
    def meta_name(self):
        return super().meta_name
    
    @property
    def meta_groups(self):
        return []
    
    #TODO: rename to main?
    @property
    def meta_main(self):
        if self.meta_module:
            return self.meta_module.meta_main
        else:
            return self
        
    @property
    def meta_attributes(self):
        return ModuleAttributes(self)