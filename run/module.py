import inspect
from abc import ABCMeta
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

    @property
    def attributes(self):
        return ModuleAttributes(self)


class ModuleBuilder(AttributeBuilder):
        
    #Protected
    
    def _make_object(self):
        cls = self._make_new_class()
        user_kwargs = self._make_user_kwargs()
        return cls(*self._args, **user_kwargs)
    
    def _make_new_class(self):
        name = self._make_name()
        bases = self._make_bases()
        dct = self._make_dict()
        return ModuleMeta(name, bases, dct)
    
    def _make_name(self):
        return self._class.__name__+'Builded'
    
    def _make_bases(self):
        return (self._class,)
    
    def _make_dict(self):
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
