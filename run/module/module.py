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
        """Return module's attributes dict-like object.
        """
        return ModuleAttributes(self)
    
    @property
    def meta_basedir(self):
        return self._meta_params.get('basedir', 
            os.path.dirname(inspect.getfile(type(self.meta_main_module))))
            
    @property
    def meta_is_main_module(self):
        """Return if module is main module.
        """
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
            return self._default_main_module_name
 
    @property
    def meta_tags(self):
        """Return module's tag list.
        """        
        return []
    
    def list(self, attribute=None):
        """Print attributes.
        """
        if attribute:
            attribute = self.meta_attributes[attribute]
        else:
            attribute = self
        names = []
        if isinstance(attribute, Module):
            for attribute in attribute.meta_attributes.values():
                names.append(attribute.meta_qualname)
            for name in sorted(names):
                self._print_function(name)
        else:
            raise TypeError(
                'Attribute "{attribute}" is not a module.'.
                format(attribute=attribute))

    def info(self, attribute=None):
        """Print information.
        """
        if attribute:
            attribute = self.meta_attributes[attribute]
        else:
            attribute = self
        self._print_function(attribute.meta_info)
        
    def meta(self, attribute=None):
        """Print metadata.
        """
        if attribute:
            attribute = self.meta_attributes[attribute]
        else:
            attribute = self
        meta = OrderedDict()
        for name in sorted(dir(attribute)):
            if name.startswith('meta_'):
                key = name.replace('meta_', '')
                meta[key] = getattr(attribute, name)
        self._pprint_function(meta)
      
    default = NullTask(
        require=['list'],
    )
    
    #Protected
    
    _print_function = staticmethod(print)    
    _pprint_function = staticmethod(pprint)