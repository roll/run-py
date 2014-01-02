import inspect
from abc import abstractmethod
from ..settings import settings
from .metaclass import AttributeMetaclass

#TODO: add basedir
#TODO: add is_bound
class Attribute(metaclass=AttributeMetaclass):
    
    #Public
    
    def __meta_init__(self, args, kwargs):
        self.__module = kwargs.pop('module', None)
        self.__signature = kwargs.pop('signature', None)
        self.__docstring = kwargs.pop('docstring', None)
    
    def __repr__(self):
        return '<{type} "{qualname}">'.format(
            type=self.meta_type, qualname=self.meta_qualname)
        
    @abstractmethod
    def __get__(self, module, module_class=None):
        pass #pragma: no cover
    
    @abstractmethod
    def __set__(self, module, value):
        pass #pragma: no cover
        
    @property
    def meta_module(self):
        return self.__module
    
    @meta_module.setter
    def meta_module(self, module):
        self.__module = module
    
    @property
    def meta_type(self):
        return type(self).__name__
    
    #TODO: remove and in if?
    @property
    def meta_qualname(self):
        if (self.meta_module and 
            self.meta_module.meta_name != 
            settings.default_main_module_name):
            if self.meta_module.meta_is_main_module:
                pattern = '[{module_name}] {name}'
            else:
                pattern = '{module_name}.{name}'
            return pattern.format(
                module_name=self.meta_module.meta_name, 
                name=self.meta_name)
        else:
            return self.meta_name
        
    @property
    def meta_name(self):
        name = ''
        if self.meta_module:
            attributes = self.meta_module.meta_attributes
            for key, attribute in attributes.items():
                if attribute == self:
                    name = key
        return name

    @property
    def meta_info(self):
        lines = []
        if self.meta_signature:
            lines.append(self.meta_signature)
        if self.meta_docstring:
            lines.append(self.meta_docstring)
        return '\n'.join(lines)

    @property
    def meta_signature(self):
        if self.__signature:
            return self.__signature
        else:
            return self.meta_qualname    
    
    @property
    def meta_docstring(self):
        if self.__docstring:
            return self.__docstring
        else:
            return inspect.getdoc(self)         