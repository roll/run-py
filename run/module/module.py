import os
import inspect
from pprint import pprint
from collections import OrderedDict
from ..attribute import Attribute
from ..task import NullTask
from .attributes import ModuleAttributes
from .metaclass import ModuleMetaclass

class Module(Attribute, metaclass=ModuleMetaclass):
    
    #Public
        
    def __meta_bind__(self, module):
        super().__meta_bind__(module)
        for attribute in self.meta_attributes.values():
            attribute.__meta_bind__(self)
    
    def __meta_init__(self):
        super().__meta_init__()
        for attribute in self.meta_attributes.values():
            attribute.__meta_init__()  
                
    def __meta_ready__(self):
        super().__meta_ready__()
        for attribute in self.meta_attributes.values():
            attribute.__meta_ready__()            
        
    def __get__(self, module=None, module_class=None):
        return self
    
    def __set__(self, module, value):
        raise AttributeError(
            'Attribute is module "{module}" '
            'and can\'t be set to any value'.
            format(module=self))
    
    def __getattr__(self, name):
        try:
            attribute = self.meta_attributes[name]
            attribute_value = attribute.__get__(attribute.meta_module)
            return attribute_value
        except KeyError:
            raise AttributeError(
                'Module "{module}" has no attribute "{name}"'.
                format(module=self, name=name))
            
    @property
    def meta_attributes(self):
        return ModuleAttributes(self)
    
    @property
    def meta_basedir(self):
        return os.path.dirname(
            inspect.getfile(type(self.meta_main_module)))
    
    @property
    def meta_is_main_module(self):
        if self.meta_module:
            return False
        else:
            return True
        
    @property
    def meta_main_module(self):
        if self.meta_module:
            return self.meta_module.meta_main_module
        else:
            return self
        
    @property
    def meta_name(self):
        if super().meta_name:
            return super().meta_name
        else:
            return self._meta_default_main_module_name
 
    @property
    def meta_tags(self):
        return []
    
    def list(self, attribute=None):
        "Print attributes"
        if attribute:
            attribute = self.meta_attributes[attribute]
        else:
            attribute = self
        names = []
        if isinstance(attribute, Module):
            for attribute in attribute.meta_attributes.values():
                names.append(attribute.meta_qualname)
            for name in sorted(names):
                self._meta_print_function(name)
        else:
            raise TypeError(
                'Attribute "{attribute}" is not a module.'.
                format(attribute=attribute))

    def info(self, attribute=None):
        "Print information"
        if attribute:
            attribute = self.meta_attributes[attribute]
        else:
            attribute = self
        self._meta_print_function(attribute.meta_info)
        
    def meta(self, attribute=None):
        "Print metadata"
        if attribute:
            attribute = self.meta_attributes[attribute]
        else:
            attribute = self
        meta = OrderedDict()
        for name in sorted(dir(attribute)):
            if name.startswith('meta_'):
                key = name.replace('meta_', '')
                meta[key] = getattr(attribute, name)
        self._meta_pprint_function(meta)
      
    default = NullTask(
        require=['list'],
    )
    
    #Protected
    
    _meta_print_function = staticmethod(print)    
    _meta_pprint_function = staticmethod(pprint)