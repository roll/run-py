import inspect
from abc import ABCMeta
from lib31.python import cachedproperty
from .attribute import Attribute, AttributeBuilder
from .task import MethodTask
from .var import PropertyVar, ValueVar

class ModuleMeta(ABCMeta):
     
    #Public
     
    def __new__(cls, name, bases, dct):
        for key, attr in dct.items():
            if (not key.startswith('_') and
                not key == 'attributes' and
                not isinstance(attr, type) and
                not isinstance(attr, Attribute) and
                not isinstance(attr, AttributeBuilder)):
                if callable(attr):
                    attr = MethodTask(attr)
                elif inspect.isdatadescriptor(attr):
                    attr = PropertyVar(attr)
                else:
                    attr = ValueVar(attr)
                dct[key] = attr
        return super().__new__(cls, name, bases, dct)
     
    
class Module(Attribute, metaclass=ModuleMeta):
    
    #Public
    
    def __new__(cls, *args, **kwargs):
        return ModuleBuilder(cls, *args, **kwargs)
    
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


class ModuleBuilder(AttributeBuilder):
    
    #Public
    
    def __call__(self):
        return self._new_class(*self._args, **self._kwargs)
        
    #Protected
    
    @property
    def _new_class(self):
        return ModuleMeta(self._name, self._bases, self._dict)
    
    @property
    def _name(self):
        return self._class.__name__+'Builded'
    
    @property
    def _bases(self):
        return (self._class,)
    
    @property
    def _dict(self):
        dct = {}
        for cls in reversed(self._class.mro()):
            for key, attr in cls.__dict__.items():
                if isinstance(attr, AttributeBuilder):
                    dct[key] = attr()
        dct['__module__'] = self._class.__module__
        dct['__new__'] = lambda cls, *args, **kwargs: object.__new__(cls)            
        return dct


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