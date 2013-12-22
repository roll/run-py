import inspect
from abc import ABCMeta, abstractmethod

class AttributeBuilder:
    
    #Public
    
    def __init__(self, cls, *args, **kwargs):
        super().__setattr__('_class', cls)
        super().__setattr__('_args', args)
        super().__setattr__('_kwargs', kwargs)
        super().__setattr__('_updates', [])
        
    def __call__(self):
        obj = self._create_object()
        self._init_object(obj)
        self._update_object(obj)
        return obj
    
    def __getattr__(self, name):
        try:
            return getattr(self._class, name)
        except AttributeError:
            raise AttributeError(name) from None
        
    def __setattr__(self, name, value):
        self._add_delayed_set(name, value)        
    
    #Protected
             
    def _create_object(self):
        return object.__new__(self._class)
        
    def _init_object(self, obj):
        obj.__system_init__(self._args, self._kwargs)
        obj.__init__(*self._args, **self._kwargs)
     
    def _update_object(self, obj):
        for update in self._updates:
            update.apply(obj)


class AttributeBuilderUpdate(metaclass=ABCMeta):
    
    #Public
    
    def apply(self, obj):
        pass #pragma: no cover


class AttributeBuilderSet(AttributeBuilderUpdate):
    
    #Public
    
    def __init__(self, name, value):
        self._name = name
        self._value = value
    
    def apply(self, obj):
        setattr(obj, self._name, self._value)
    
    
class AttributeBuilderCall(AttributeBuilderUpdate):
    
    #Public
    
    def __init__(self, name, *args, **kwargs):
        self._name = name
        self._args = kwargs
        self._kwargs = kwargs
        
    def apply(self, obj):
        method = getattr(obj, self._name)
        method(*self._args, **self.kwarg)


class AttributeMeta(ABCMeta):
    
    #Public
    
    def __call__(self, *args, **kwargs):
        builder = self._builder_class(self, *args, **kwargs)
        if 'module' in kwargs:
            return builder()
        else:
            return builder
        
    #Protected
    
    _builder_class = AttributeBuilder    
       
        
class Attribute(metaclass=AttributeMeta):
    
    #Public
    
    def __system_init__(self, args, kwargs):
        self.__module = kwargs.pop('module', None)
        self.__signature = kwargs.pop('signature', None)
        self.__docstring = kwargs.pop('docstring', None)
    
    @abstractmethod
    def __get__(self, module, module_class):
        pass #pragma: no cover
    
    def __set__(self, module, value):
        raise RuntimeError('Can\'t set attribute')
        
    @property
    def module(self):
        return self.__module
    
    @module.setter
    def module(self, module):
        self.__module = module
    
    @property
    def metadata(self):
        return AttributeMetadata(
            self, signature=self.__signature, 
                  docstring=self.__docstring)
        
  
class AttributeMetadata:
    
    #Public
    
    def __init__(self, attribute, signature=None, docstring=None):
        self._attribute = attribute
        self._signature = signature
        self._docstring = docstring

    @property
    def name(self):
        return '.'.join(filter(None, 
            [self.module_name, self.attribute_name]))
    
    @property
    def module_name(self):
        if self._attribute.module:
            return self._attribute.module.metadata.name 
        else:
            return ''  
    
    @property
    def attribute_name(self):
        if self._attribute.module:
            return (self._attribute.module.attributes.
                    find(self._attribute, default='')) 
        else:
            return '' 

    @property
    def help(self):
        return '\n'.join(filter(None, 
            [self.signature, self.docstring]))

    @property
    def signature(self):
        if self._signature:
            return self._signature
        else:
            return self.name    
    
    @property
    def docstring(self):
        if self._docstring:
            return self._docstring
        else:
            return inspect.getdoc(self._attribute)   