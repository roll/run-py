import inspect
from abc import ABCMeta, abstractmethod

class AttributeBuilder:
    
    #Public
    
    def __init__(self, cls, *args, **kwargs):
        super().__setattr__('_class', cls)
        super().__setattr__('_args', args)
        super().__setattr__('_kwargs', kwargs)
        super().__setattr__('_delayed_sets', [])
        super().__setattr__('_delayed_calls', [])
        
    def __call__(self):
        obj = self._make_object()
        self._process_system_init(obj)
        self._process_delayed_sets(obj)
        self._process_delayed_calls(obj)
        return obj
    
    def __getattr__(self, name):
        try:
            return getattr(self._class, name)
        except:
            raise AttributeError(name) from None
        
    def __setattr__(self, name, value):
        self._add_delayed_set(name, value)        
    
    #Protected
    
    _system_init_classes = property(lambda self: [Attribute])
    _system_kwarg_keys = ['signature', 'docstring']
    
    def _process_delayed_calls(self, obj):
        for call in self._delayed_calls:
            method = getattr(obj, call[0])
            method(*call[1], **call[2])
    
    def _process_delayed_sets(self, obj):
        for st in self._delayed_sets:
            setattr(obj, st[0], st[1])
    
    def _process_system_init(self, obj):
        system_kwargs = self._make_system_kwargs()
        for cls in self._system_init_classes:
            cls.__init__(obj, **system_kwargs) 

    def _make_system_kwargs(self):
        return {key: value for key, value in self._kwargs.items()
                if key in self._system_kwarg_keys}
                
    def _make_object(self):
        user_kwargs = self._make_user_kwargs()
        obj = object.__new__(self._class)
        obj.__init__(*self._args, **user_kwargs)
        return obj

    def _make_user_kwargs(self):
        return {key: value for key, value in self._kwargs.items()
                if key not in self._system_kwarg_keys}
    
    def _add_delayed_call(self, name, args, kwargs):
        self._delayed_calls.append((name, args, kwargs))
        
    def _add_delayed_set(self, name, value):
        self._delayed_sets.append((name, value))
        
        
class Attribute(metaclass=ABCMeta):
    
    #Public
    
    def __new__(cls, *args, **kwargs):
        builder = cls._builder_class(cls, *args, **kwargs)
        if 'module' not in kwargs:
            return builder
        else:
            return builder()
    
    def __init__(self, *args, **kwargs):
        self.__module = None
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
        
    #Protected
    
    _builder_class = AttributeBuilder
        
  
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