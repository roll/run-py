from pprint import pprint
from collections import OrderedDict
from ..attribute import Attribute
from ..settings import settings
from ..task import Task
from .metaclass import ModuleMetaclass

class Module(Attribute, metaclass=ModuleMetaclass):
    
    #Public
    
    def __meta_init__(self, args, kwargs):
        super().__meta_init__(args, kwargs)
        for attribute in self.meta_attributes.values():
            attribute.meta_module = self
        
    def __get__(self, module, module_class=None):
        return self
    
    def __set__(self, module, value):
        raise AttributeError(
            'Attribute "{name}" is module '
            '"{module}" and can\'t be set'.
            format(name=self.meta_name, module=self))
    
    def __getattr__(self, name):
        if '.' in name:
            #TODO: it works also for no module attributes
            #like default.meta_name or __getattr__.__doc__
            module_name, attribute_name = name.split('.', 1)
            module = getattr(self, module_name)
            attribute = getattr(module, attribute_name)
            return attribute
        else:
            raise AttributeError(
                'No attribute "{name}" '
                'in module "{qualname}"'.format(
                name=name, qualname=self.meta_qualname))
    
    @property
    def meta_name(self):
        if super().meta_name:
            return super().meta_name
        else:
            return self._meta_default_main_module_name
        
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
        attributes = {}
        for name, attr in vars(type(self)).items():
            if isinstance(attr, Attribute):
                attributes[name] = attr
        return attributes
    
    @property
    def meta_tags(self):
        return []
        
    #TODO: refactor list, info, meta (add "attr.attr" support)
        
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
            self._meta_print_operator(name)

    def info(self, attribute=None):
        "Print information"
        if attribute and attribute in self.meta_attributes:
            attribute = self.meta_attributes[attribute]
            self._meta_print_operator(attribute.meta_info)
        else:
            self._meta_print_operator(self.meta_info)
        
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
        self._meta_formatted_print_operator(meta)
      
    default = Task(
        require=['list'],
    )
    
    #Protected
    
    _meta_default_main_module_name = settings.default_main_module_name
    _meta_formatted_print_operator = staticmethod(pprint)
    _meta_print_operator = staticmethod(print)