from lib31.python import cachedproperty
from .attribute import Attribute

class Module(Attribute):
    
    #Public
    
    def __init__(self, *args, **kwargs):
        for attribute in self.attributes.values():
            attribute.module = self
        super().__init__(*args, **kwargs)
        
    def __get__(self, module, module_class):
        return self
    
    def __getattr__(self, name):
        try:
            module_name, attribute_name = name.split('.', 1)
        except ValueError:
            raise AttributeError(name)
        module = getattr(self, module_name)
        attribute = getattr(module, attribute_name)
        return attribute

    @cachedproperty
    def attributes(self):
        return ModuleAttributes(self)


class ModuleAttributes(dict):
    
    #Public
    
    def __init__(self, module):
        for cls in reversed(module.__class__.mro()):
            for name, attr in cls.__dict__.items():
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