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
    
    def __repr__(self):
        try:
            return '<{category} "{qualname}">'.format(
                category=self.meta_type, 
                qualname=self.meta_qualname)
        except Exception:
            return super().__repr__()
    
    @property
    def meta_basedir(self):
        """Attribute's basedir.
           
        If meta_chdir is True some type of attributes (tasks, vars)
        change current directory to meta_basedir when invoking.
           
        This property is:
        
        - initable/writable
        - inherited from module
        """        
        return self._meta_params.get('basedir', 
           self.meta_module.meta_basedir)
        
    @meta_basedir.setter
    def meta_basedir(self, value):
        self._meta_params['basedir'] = value
    
    @property
    def meta_cache(self):
        """Attribute's caching status (enabled or disabled).
        
        If meta_cache is True some type of attributes (vars)
        cache results after first invocation.        
           
        This property is:
        
        - initable/writable
        - inherited from module
        """ 
        return self._meta_params.get('cache', 
            self.meta_module.meta_cache)
    
    @meta_cache.setter
    def meta_cache(self, value):
        self._meta_params['cache'] = value
           
    @property
    def meta_chdir(self):
        """Attribute's chdir status (enabled or disabled).
        
        .. seealso:: :attr:`run.Attribute.meta_basedir`
        
        This property is:
        
        - initable/writable
        - inherited from module
        """     
        return self._meta_params.get('chdir', 
            self.meta_module.meta_chdir)            
        
    @meta_chdir.setter   
    def meta_chdir(self, value):
        self._meta_params['chdir'] = value
       
    @property
    def meta_dispatcher(self):
        """Attribute's dispatcher.
        
        Dispatcher has been using to operate signals.
           
        This property is:
        
        - initable/writable
        - inherited from module
        """         
        return self._meta_params.get('dispatcher', 
            self.meta_module.meta_dispatcher)
        
    @meta_dispatcher.setter
    def meta_dispatcher(self, value):
        self._meta_params['dispatcher'] = value
    
    @property
    def meta_docstring(self):
        """Attribute's docstring.
        
        This property is:
        
        - initable/writable
        """        
        return self._meta_params.get('docstring', 
            inspect.getdoc(self))        
    
    @meta_docstring.setter
    def meta_docstring(self, value):
        self._meta_params['docstring'] = value
    
    @property
    def meta_fallback(self):
        """Attribute's fallback.
        
        In some attributes (tasks) fallback has been using when
        attribute invocation fails. 
        
        This property is:
        
        - initable/writable
        - inherited from module
        """        
        return self._meta_params.get('fallback', 
            self.meta_module.meta_fallback)  
    
    @meta_fallback.setter   
    def meta_fallback(self, value):
        self._meta_params['fallback'] = value        
        
    @property
    def meta_info(self):
        """Attribute's info as a string.
           
        It's a combination of signature and docstring.
        """
        lines = []
        if self.meta_signature:
            lines.append(self.meta_signature)
        if self.meta_docstring:
            lines.append(self.meta_docstring)
        return '\n'.join(lines)
   
    @property
    def meta_main_module(self):
        """Attribute's main module of module hierarchy.
        """          
        return self.meta_module.meta_main_module            
    
    @property
    def meta_module(self):
        """Attribute's module. 
        """         
        return self._meta_module
        
    @property
    def meta_name(self):
        """Attribute's name. 
           
        Name is defined as attribute name in module.
        If module is None name will be empty string. 
        """ 
        name = ''
        attributes = self.meta_module.meta_attributes
        for key, attribute in attributes.items():
            if attribute is self:
                name = key
        return name
      
    @property
    def meta_qualname(self):
        """Attribute's qualified name.
           
        Qualname combines module name and attribute name.
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
        """Attribute's signature.
        
        This property is:
        
        - initable/writable
        """        
        return self._meta_params.get('signature', 
            self.meta_qualname)
    
    @meta_signature.setter   
    def meta_signature(self, value):
        self._meta_params['signature'] = value
        
    @property
    def meta_type(self):
        """Attribute's type as a string. 
        """ 
        return type(self).__name__
    
    #Protected
    
    _default_main_module_name = settings.default_main_module_name