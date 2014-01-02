import inspect
from abc import abstractmethod
from ..settings import settings
from .metaclass import AttributeMetaclass

class Attribute(metaclass=AttributeMetaclass):
    
    #Public
    
    def __meta_init__(self, args, kwargs):
        self.__module = kwargs.pop('module', None)
        self.__dispatcher = kwargs.pop('dispatcher', None)
        self.__basedir = kwargs.pop('basedir', None)        
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
        if self.meta_is_bound:
            #TODO: improve message
            raise AttributeError('Cant\'t set attribute')
        else:
            self.__module = module
     
    @property
    def meta_is_bound(self):
        if self.meta_module:
            attributes = self.meta_module.meta_attributes
            for _, attribute in attributes.items():
                    if attribute == self:
                        return True
        return False      
       
    @property
    def meta_dispatcher(self):
        if self.__dispatcher:
            return self.__dispatcher
        elif self.meta_module:
            return self.meta_module.meta_dispatcher
        else:
            from ..dispatcher import NullDispatcher
            self.__dispatcher = NullDispatcher()
            return self.__dispatcher
    
    @property
    def meta_basedir(self):
        if self.__basedir:
            return self.__basedir
        elif self.meta_module:
            return self.meta_module.meta_basedir
    
    #TODO: fix qualname with main_module [] issue
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
    
    @property
    def meta_type(self):
        return type(self).__name__        