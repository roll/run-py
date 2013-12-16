import inspect
import importlib
from abc import ABCMeta
from lib31.python import cachedproperty
from .attribute import Attribute
from .unit import Unit

class NamespaceMeta(ABCMeta):
   
    #Public
   
    def __new__(cls, name, bases, attrs):
        for name, attr in attrs.items():
            if (not name.startswith('_') and
                not name == 'attributes'):
                if (not isinstance(attr, type) and
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
    def __import(cls, module_name, attr_name):
        package_name = inspect.getmodule(cls).__package__
        module = importlib.import_module('.'+module_name, package_name)
        attr = getattr(module, attr_name)
        return attr  


class Namespace(Unit, metaclass=NamespaceMeta):
    
    #Public
    
    def __init__(self, *args, **kwargs):
        for attribute in self.attributes.values():
            attribute.namespace = self
        super().__init__(*args, **kwargs)
    
    def __getattr__(self, name):
        try:
            namespace_name, attribute_name = name.split('.', 1)
        except ValueError:
            raise AttributeError(name)
        namespace = getattr(self, namespace_name)
        attribute = getattr(namespace, attribute_name)
        return attribute

    @cachedproperty
    def attributes(self):
        return NamespaceAttributes(self)


class NamespaceAttributes(dict):
    
    #Public
    
    def __init__(self, namespace):
        for cls in reversed(namespace.__class__.mro()):
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