import inspect
from copy import copy
from abc import abstractmethod
from ..settings import settings
from .metaclass import AttributeMetaclass

class Attribute(metaclass=AttributeMetaclass):
    
    #Public
    
    def __meta_build__(self, builder):
        self._meta_builder = builder
        self._meta_args = copy(builder.meta_args)
        self._meta_kwargs = copy(builder.meta_kwargs)
        self._meta_updates = copy(builder.meta_updates)        
        self._meta_ready = False
        
    def __meta_bind__(self, module):
        self._meta_module = module
        
    def __meta_init__(self):
        args = self._meta_args
        kwargs = self._meta_kwargs
        if kwargs.get('is_expand', True):
            self._meta_expand(args)
            self._meta_expand(kwargs)
        self._meta_basedir = kwargs.pop('basedir', None)
        self._meta_dispatcher = kwargs.pop('dispatcher', None)   
        self._meta_docstring = kwargs.pop('docstring', None)
        self._meta_is_chdir = kwargs.pop('is_chdir', True)
        self._meta_is_expand = kwargs.pop('is_expand', True)
        self._meta_signature = kwargs.pop('signature', None)
        self.__init__(*self._meta_args, **self._meta_kwargs)
    
    def __meta_update__(self):
        for update in self._meta_updates:
            update.apply(self) 
        
    def __meta_ready__(self):
        self._meta_ready = True      
      
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
        if self._meta_ready:
            return '<{category} "{qualname}">'.format(
                category=self.meta_type, 
                qualname=self.meta_qualname)
        return super().__repr__()
    
    @property
    def meta_basedir(self):
        if self._meta_basedir != None:
            return self._meta_basedir
        else:
            return self.meta_module.meta_basedir
        
    @property
    def meta_builder(self):
        if self._meta_builder != None:
            return self._meta_builder
        else:
            raise ValueError(
                'Attribute "{attribute}" has no assotiated builder'.
                format(attribute=self))
            
    @property
    def meta_context(self):
        return self.meta_main_module                     
       
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
    def meta_is_chdir(self):
        return self._meta_is_chdir
    
    @property
    def meta_is_expand(self):
        return self._meta_is_expand  
   
    @property
    def meta_main_module(self):
        return self.meta_module.meta_main_module            
    
    @property
    def meta_module(self):
        if self._meta_module == None:
            self._meta_module = self._meta_null_module_class(module=None)
        return self._meta_module
        
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
        #Cycle dependency if static
        from ..module import NullModule
        return NullModule
    
    def _meta_expand(self, args):
        try:
            iterator = args.items()
        except AttributeError:
            iterator = enumerate(args)
        for key, value in iterator:
            args[key] = self._meta_expand_value(value)
        return args
    
    def _meta_expand_value(self, value):
        if inspect.isdatadescriptor(value):
            value = value.__get__(self.meta_module, type(self.meta_module))
        return value    