import inspect
from abc import abstractmethod
from ..settings import settings
from .metaclass import AttributeMetaclass

class Attribute(metaclass=AttributeMetaclass):
    
    #Public
    
    def __meta_init__(self, args, kwargs):
        self._meta_basedir = kwargs.pop('basedir', None)
        self._meta_dispatcher = kwargs.pop('dispatcher', None)                 
        self._meta_module = kwargs.pop('module', None)
        self._meta_signature = kwargs.pop('signature', None)
        self._meta_docstring = kwargs.pop('docstring', None)
    
    def __repr__(self):
        try:
            return '<{type} "{qualname}">'.format(
                type=self.meta_type, 
                qualname=self.meta_qualname)
        except Exception:
            return super().__repr__()
         
    @abstractmethod
    def __get__(self, module, module_class=None):
        pass #pragma: no cover
    
    @abstractmethod
    def __set__(self, module, value):
        pass #pragma: no cover
    
    @property
    def meta_basedir(self):
        if self._meta_basedir != None:
            return self._meta_basedir
        else:
            return self.meta_module.meta_basedir
       
    @property
    def meta_dispatcher(self):
        if self._meta_dispatcher != None:
            return self._meta_dispatcher
        else:
            return self.meta_module.meta_dispatcher
    
    @property
    def meta_docstring(self):
        if self._meta_docstring != None:
            return self._meta_docstring
        else:
            return inspect.getdoc(self)

    @property
    def meta_info(self):
        lines = []
        if self.meta_signature:
            lines.append(self.meta_signature)
        if self.meta_docstring:
            lines.append(self.meta_docstring)
        return '\n'.join(lines)
     
    @property
    def meta_is_bound(self):
        attributes = self.meta_module.meta_attributes
        for attribute in attributes.values():
            if attribute == self:
                return True
        return False   
              
    @property
    def meta_module(self):
        if self._meta_module == None:
            self._meta_module = self._meta_null_module_class(module=None)
        return self._meta_module
    
    @meta_module.setter
    def meta_module(self, module):
        if self.meta_is_bound:
            raise AttributeError(
                'Can\'t set meta_module in Attribute "{attribute}" '
                'because it is already bound to module "{module}"'.
                format(attribute=self, module=self.meta_module))
        else:
            self._meta_module = module
        
    @property
    def meta_name(self):
        name = ''
        attributes = self.meta_module.meta_attributes
        for key, attribute in attributes.items():
            if attribute is self:
                name = key
        return name
      
    @property
    def meta_qualname(self):
        if self.meta_module.meta_is_main_module:
            if (self.meta_module.meta_name ==
                self._meta_default_main_module_name):
                pattern = '{name}'
            else:
                pattern = '[{module_qualname}] {name}'
        else:
            pattern = '{module_qualname}.{name}'
        return pattern.format(
            module_qualname=self.meta_module.meta_qualname,
            name=self.meta_name)

    @property
    def meta_signature(self):
        if self._meta_signature != None:
            return self._meta_signature
        else:
            return self.meta_qualname    
    
    @property
    def meta_type(self):
        return type(self).__name__
    
    #Protected
    
    _meta_default_main_module_name = settings.default_main_module_name
    
    @property
    def _meta_null_module_class(self):
        from ..module import NullModule
        return NullModule