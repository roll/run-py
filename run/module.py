import inspect
import importlib
from abc import ABCMeta
from lib31.python import cachedproperty
from .attribute import Attribute

class ModuleMeta(ABCMeta):
   
    #Public
   
    def __new__(cls, name, bases, attrs):
        for name, attr in attrs.items():
            if (not name.startswith('_') and
                not name == 'attributes' and
                not isinstance(attr, type) and
                not isinstance(attr, Attribute)):
                    if callable(attr):
                        MethodTask = cls.__import('task', 'MethodTask')
                        attrs[name] = MethodTask(attr)
                    elif inspect.isdatadescriptor(attr):
                        PropertyVar = cls.__import('var', 'PropertyVar')
                        attrs[name] = PropertyVar(attr)
                    else:
                        ValueVar = cls.__import('var', 'ValueVar')
                        attrs[name] = ValueVar(attr)
        return super().__new__(cls, name, bases, attrs)
    
    #Private
        
    @classmethod
    def __import(cls, module_name, attribute_name):
        package_name = inspect.getmodule(cls).__package__
        module = importlib.import_module('.'+module_name, package_name)
        attr = getattr(module, attribute_name)
        return attr  


class Module(Attribute, metaclass=ModuleMeta):
    
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