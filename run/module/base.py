import os
import inspect
from ..attribute import Attribute
from ..settings import settings
from .attributes import ModuleAttributes 
from .metaclass import ModuleMetaclass

class BaseModule(Attribute, metaclass=ModuleMetaclass):
    
    #Public
    
    def __meta_init__(self, args, kwargs):
        super().__meta_init__(args, kwargs)
        for attribute in self.meta_attributes.values():
            attribute.meta_module = self
        
    def __get__(self, module=None, module_class=None):
        return self
    
    def __set__(self, module, value):
        raise AttributeError(
            'Attribute "{name}" is module '
            '"{module}" and can\'t be set'.
            format(name=self.meta_name, module=self))
    
    def __getattr__(self, name):
        try:
            attribute = self.meta_attributes[name]
            attribute_value = attribute.__get__(attribute.meta_module)
            return attribute_value
        except KeyError:
            raise AttributeError(
                'No attribute "{name}" '
                'in module "{qualname}"'.format(
                name=name, qualname=self.meta_qualname))
            
    @property
    def meta_attributes(self):
        return ModuleAttributes(self)
    
    #TODO: fix opportunity to set basedir
    @property
    def meta_basedir(self):
        return os.path.dirname(inspect.getfile(type(self.meta_main_module)))
    
    @property
    def meta_is_main_module(self):
        if self == self.meta_main_module:
            return True
        else:
            return False
        
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
 
#     TODO: fix
#     @property
#     def meta_tags(self):
#         return []
    meta_tags = []
    
    #Protected
    
    _meta_default_main_module_name = settings.default_main_module_name