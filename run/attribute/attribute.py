import inspect
from abc import ABCMeta, abstractmethod
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
    
    def __set__(self, module, value):
        raise AttributeError('Can\'t set attribute')
    
    def __repr__(self):
        return '<{type} "{name}">'.format(
            type=self.meta_type, name=self.meta_name)
        
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
    def meta_name(self):
        name = ''
        if self.meta_module_name:
            if self.meta_module.meta_is_main_module:
                name += '['+self.meta_module_name+'] '
            else:
                name += self.meta_module_name+'.'
        name += self.meta_attribute_name
        return name
    
    @property
    def meta_module_name(self):
        if self.meta_module:
            return self.meta_module.meta_name
        else:
            return ''
    
    @property
    def meta_attribute_name(self):
        if self.meta_module:
            return (self.meta_module.meta_attributes.find(self, default='')) 
        else:
            return ''

    @property
    def meta_help(self):
        lines = filter(None, [self.meta_signature, self.meta_docstring])
        return '\n'.join(lines)

    @property
    def meta_signature(self):
        if self.__signature:
            return self.__signature
        else:
            return self.meta_name    
    
    @property
    def meta_docstring(self):
        if self.__docstring:
            return self.__docstring
        else:
            return inspect.getdoc(self)   