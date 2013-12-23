__all__ = ['ModuleAttributes']

from ..attribute import Attribute

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