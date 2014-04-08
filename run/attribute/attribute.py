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
        self._meta_basedir = kwargs.pop('meta_basedir', None)
        self._meta_chdir = kwargs.pop('meta_chdir', True)
        self._meta_dispatcher = kwargs.pop('meta_dispatcher', None)   
        self._meta_docstring = kwargs.pop('meta_docstring', None)
        self._meta_signature = kwargs.pop('meta_signature', None)
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
    
    #TODO: with Module.__getattr__ it brings strange errors
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
           
        Property resolving order:
           
        - attribute's value (initiable, writable)
        - module's value
        """        
        if self._meta_basedir != None:
            return self._meta_basedir
        else:
            return self.meta_module.meta_basedir
        
    @meta_basedir.setter
    def meta_basedir(self, value):
        self._meta_basedir = value
   
    @property
    def meta_chdir(self):
        """Return attribute's change directory flag. 
        
        .. seealso:: :attr:`run.Attribute.meta_basedir`
        
        Property resolving order:
           
        - attribute's value (initiable, writable)
        - module's value
        """     
        if self._meta_chdir != None:
            return self._meta_chdir
        else:
            return self.meta_module.meta_chdir                
        
    @meta_chdir.setter   
    def meta_chdir(self, value):
        self._meta_chdir = value
       
    @property
    def meta_dispatcher(self):
        """Return attribute's dispatcher.
        
        Dispatcher has been using to operate signals.
           
        Property resolving order:
           
        - attribute's value (initiable, read-only)
        - module's value
        """         
        if self._meta_dispatcher != None:
            return self._meta_dispatcher
        else:
            return self.meta_module.meta_dispatcher
    
    @property
    def meta_docstring(self):
        """Return attribute's docstring.
           
        Property resolving order:
           
        - attribute's value (initiable, read-only)
        - attribute inspection
        """        
        if self._meta_docstring != None:
            return self._meta_docstring
        else:
            return inspect.getdoc(self)
    
    @property
    def meta_info(self):
        """Return attribute's info as string.
           
        By default it's a combination of signature and docstring.
        
        Property resolving order:
           
        - attribute inspection
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
           
        Property resolving order:
           
        - module's value
        """          
        return self.meta_module.meta_main_module            
    
    @property
    def meta_module(self):
        """Return attribute's module. 
           
        If attribute has been created with module it returns module.
        In other case it returns None.
           
        Property resolving order:
           
        - attribute's value (initiable, read-only)
        """         
        return self._meta_module
        
    @property
    def meta_name(self):
        """Return attribute's name. 
           
        Name is defined as attribute name in attribute module.
        If module is None name will be empty string.
           
        Property resolving order:
           
        - attribute inspection
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
           
        Qualname includes module name and attribute name.
        
        Property resolving order:
           
        - attribute inspection
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
           
        - attribute's value (initiable, read-only)
        - attribute inspection
        """ 
        if self._meta_signature != None:
            return self._meta_signature
        else:
            return self.meta_qualname
    
    @property
    def meta_type(self):
        """Return attribute's type as string. 
           
        Property resolving order:
           
        - attribute inspection
        """ 
        return type(self).__name__
    
    #Protected
    
    _default_main_module_name = settings.default_main_module_name