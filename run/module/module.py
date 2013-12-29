import inspect
from pprint import pprint
from collections import OrderedDict
from ..attribute import AttributeBuilder, AttributeMetaclass, Attribute
from ..settings import settings
from ..task import Task, MethodTask
from ..var import ValueVar, PropertyVar
from .attributes import ModuleAttributes
from .builder import ModuleBuilder

class ModuleMetaclass(AttributeMetaclass):
     
    #Public
     
    def __new__(cls, name, bases, dct):
        for key, attr in dct.items():
            if (not key.startswith('_') and
                not key.startswith('meta_') and
                not isinstance(attr, type) and
                not isinstance(attr, Attribute) and
                not isinstance(attr, AttributeBuilder)):
                if callable(attr):
                    dct[key] = MethodTask(attr)
                elif inspect.isdatadescriptor(attr):
                    dct[key] = PropertyVar(attr)
                else:
                    dct[key] = ValueVar(attr)
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
    
    def __set__(self, module, value):
        raise AttributeError(
            'Attribute "{0}" is module "{1}" and can\'t be set'.
            format(self._name, self))
    
    def __getattr__(self, name):
        try:
            module_name, attribute_name = name.split('.', 1)
        except ValueError:
            raise AttributeError(
                'No attribute "{0}" in module "{1}"'.
                format(name, self.meta_qualname)) from None
        module = getattr(self, module_name)
        attribute = getattr(module, attribute_name)
        return attribute
    
    #TODO: decide about meta_* to attribute or module
    
    @property
    def meta_main_module(self):
        if self.meta_module:
            return self.meta_module.meta_main_module
        else:
            return self
        
    @property
    def meta_is_main_module(self):
        if self == self.meta_main_module:
            return True
        else:
            return False
            
    @property
    def meta_attributes(self):
        return ModuleAttributes(self)
   
    @property
    def meta_name(self):
        if super().meta_name:
            return super().meta_name
        else:
            return settings.default_main_module_name
    
    @property
    def meta_tags(self):
        return []
        
    #TODO: list, info, meta now supports only 
    #the module attributes (not base.render)
    
    #TODO: "if attribute and attribute in self.meta_attributes"
    #works bad for attribute not in self.meta_attributes
        
    def list(self, attribute=None):
        "Print attributes"
        names = []
        if attribute and attribute in self.meta_attributes:
            attribute = self.meta_attributes[attribute]
            attributes = attribute.meta_attributes
        else:
            attributes = self.meta_attributes
        for attribute in attributes.values():
            names.append(attribute.meta_qualname)
        for name in sorted(names):
            print(name)

    def info(self, attribute=None):
        "Print information"
        if attribute and attribute in self.meta_attributes:
            attribute = self.meta_attributes[attribute]
            print(attribute.meta_info)
        else:
            print(self.meta_info)
        
    def meta(self, attribute=None):
        "Print metadata"
        if attribute and attribute in self.meta_attributes:
            attribute = self.meta_attributes[attribute]
        else:
            attribute = self
        meta = OrderedDict()
        for name in sorted(dir(attribute)):
            if name.startswith('meta_'):
                key = name.replace('meta_', '')
                meta[key] = getattr(attribute, name)
        pprint(meta)
      
    default = Task(
        require=['list'],
    )     