import os
import inspect
from abc import abstractmethod
from ..settings import settings
from .metaclass import AttributeMetaclass

class Attribute(metaclass=AttributeMetaclass):
    """Main base class for attributes.
    
    This class is abstract base class for every attribute
    used in run. Abstract methods: __get__, __set__.
    """
    
    #Public        
        
    def __build__(self, module, *args, **kwargs):
        self._meta_module = module
        self._meta_basedir = kwargs.get('meta_basedir', None)
        self._meta_cache = kwargs.get('meta_cache', None)        
        self._meta_chdir = kwargs.get('meta_chdir', None)
        self._meta_dispatcher = kwargs.get('meta_dispatcher', None)   
        self._meta_docstring = kwargs.get('meta_docstring', None)
        self._meta_fallback = kwargs.get('meta_fallback', None)        
        self._meta_signature = kwargs.get('meta_signature', None)
        self._meta_params = {}
        for key in list(kwargs):
            if key.startswith('meta_'):
                self._meta_params[key.lstrip('meta_')] = kwargs.pop(key)
        self.__init__(*args, **kwargs)
      
    @abstractmethod
    def __get__(self, module, module_class=None):
        pass #pragma: no cover
    
    @abstractmethod
    def __set__(self, module, value):
        pass #pragma: no cover
        
    def __enter__(self):
        return self
        
    def __exit__(self, *args, **kwargs):
        pass
    
    def __repr__(self):
        try:
            return '<{category} "{qualname}">'.format(
                category=self.meta_type, 
                qualname=self.meta_qualname)
        except Exception:
            return super().__repr__()
    
    @property
    def meta_basedir(self):
        """Return attribute's basedir.
           
        If meta_chdir is True some type of attributes (tasks, vars)
        change current directory to meta_basedir when invoking.
           
        This property is writable and inherited from module.
        """        
        basedir = self.meta_module.meta_basedir
        return self._meta_params.get('basedir', basedir)
        
    @meta_basedir.setter
    def meta_basedir(self, value):
        self._meta_params['basedir'] = value
    
    @property
    def meta_cache(self):
        """Return attribute's caching status (enabled or disabled).
        
        If meta_cache is True some type of attributes (vars)
        cache results after first invocation.        
           
        Property resolving order:
           
        - attribute's value
        - module's value
        - default: True
        """ 
        if self._meta_cache != None:
            return self._meta_cache
        elif self.meta_module.meta_cache != None:
            return self.meta_module.meta_cache
        else:
            return True
    
    @meta_cache.setter
    def meta_cache(self, value):
        self._meta_cache = value
           
    @property
    def meta_chdir(self):
        """Return attribute's chdir status (enabled or disabled).
        
        .. seealso:: :attr:`run.Attribute.meta_basedir`
        
        Property resolving order:
           
        - attribute's value
        - module's value
        - default: True
        """     
        if self._meta_chdir != None:
            return self._meta_chdir
        elif self.meta_module.meta_chdir != None:
            return self.meta_module.meta_chdir
        else:
            return True              
        
    @meta_chdir.setter   
    def meta_chdir(self, value):
        self._meta_chdir = value
       
    @property
    def meta_dispatcher(self):
        """Return attribute's dispatcher.
        
        Dispatcher has been using to operate signals.
           
        Property resolving order:
           
        - attribute's value
        - module's value
        """         
        if self._meta_dispatcher != None:
            return self._meta_dispatcher
        else:
            return self.meta_module.meta_dispatcher
        
    @meta_dispatcher.setter   
    def meta_dispatcher(self, value):
        self._meta_dispatcher = value        
    
    @property
    def meta_docstring(self):
        """Return attribute's docstring.
        
        Property resolving order:
           
        - attribute's value
        - inspection
        """        
        if self._meta_docstring != None:
            return self._meta_docstring
        else:
            return inspect.getdoc(self)
    
    @meta_docstring.setter
    def meta_docstring(self, value):
        self._meta_docstring = value 
    
    @property
    def meta_fallback(self):
        """Return attribute's fallback.
        
        Property resolving order:
           
        - attribute's value
        - module's value        
        """
        if self._meta_fallback != None:
            return self._meta_fallback
        else:
            return self.meta_module.meta_fallback
    
    @meta_fallback.setter   
    def meta_fallback(self, value):
        self._meta_fallback = value         
        
    @property
    def meta_info(self):
        """Return attribute's info as string.
           
        It's a combination of signature and docstring.
        This property is read-only.
        """
        lines = []
        if self.meta_signature:
            lines.append(self.meta_signature)
        if self.meta_docstring:
            lines.append(self.meta_docstring)
        return '\n'.join(lines)
   
    @property
    def meta_main_module(self):
        """Return attribute's main module of module hierarchy.
           
        This property is read-only.
        """          
        return self.meta_module.meta_main_module            
    
    @property
    def meta_module(self):
        """Return attribute's module. 
           
        If attribute has been created with module it returns module.
        In other case it returns None. This property is read-only.
        """         
        return self._meta_module
        
    @property
    def meta_name(self):
        """Return attribute's name. 
           
        Name is defined as attribute name in module of attribute.
        If module is None name will be empty string. 
        This property is read-only.
        """ 
        name = ''
        attributes = self.meta_module.meta_attributes
        for key, attribute in attributes.items():
            if attribute is self:
                name = key
        return name
      
    @property
    def meta_qualname(self):
        """Return attribute's qualified name.
           
        Qualname combines module name and attribute name.
        This property is read-only
        """ 
        if self.meta_module.meta_is_main_module:
            if (self.meta_module.meta_name ==
                self._default_main_module_name):
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
        """Return attribute's signature.
           
        Property resolving order:
           
        - attribute's value
        - inspection
        """ 
        if self._meta_signature != None:
            return self._meta_signature
        else:
            return self.meta_qualname
    
    @meta_signature.setter   
    def meta_signature(self, value):
        self._meta_signature = value 
        
    @property
    def meta_type(self):
        """Return attribute's type as string. 
           
        This property is read-only.
        """ 
        return type(self).__name__
    
    #Protected
    
    _default_main_module_name = settings.default_main_module_name