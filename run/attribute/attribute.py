import inspect
from abc import ABCMeta, abstractmethod
from ..settings import settings
from .builder import AttributeBuilder

class AttributeMetaclass(ABCMeta):
    
    #Public
    
    def __call__(self, *args, **kwargs):
        builder = self._builder_class(self, *args, **kwargs)
        if 'module' in kwargs:
            return builder()
        else:
            return builder
        
    #Protected
    
    _builder_class = AttributeBuilder 
    
    
class Attribute(metaclass=AttributeMetaclass):
    
    #Public
    
    def __meta_init__(self, args, kwargs):
        self.__module = kwargs.pop('module', None)
        self.__signature = kwargs.pop('signature', None)
        self.__docstring = kwargs.pop('docstring', None)
    
    @abstractmethod
    def __get__(self, module, module_class):
        pass #pragma: no cover
    
    @abstractmethod
    def __set__(self, module, value):
        pass #pragma: no cover
    
    def __repr__(self):
        return '<{type} "{qualname}">'.format(
            type=self.meta_type, name=self.meta_qualname)
        
    @property
    def meta_module(self):
        return self.__module
    
    @meta_module.setter
    def meta_module(self, module):
        self.__module = module
    
    @property
    def meta_type(self):
        return self.__class__.__name__
    
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
        if self.meta_module:
            attributes = self.meta_module.meta_attributes
            name = attributes.find(self, default='')
            return name
        else:
            return ''

    @property
    def meta_info(self):
        lines = filter(None, [
            self.meta_signature, 
            self.meta_docstring])
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