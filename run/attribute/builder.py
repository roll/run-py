from copy import copy

class AttributeBuilder:
    
    #Public
    
    def __init__(self, cls, *args, **kwargs):
        self._module = kwargs.pop('module', None)
        self._updates = kwargs.pop('updates', [])
        self._class = cls
        self._args = list(args)
        self._kwargs = kwargs
        
    def __copy__(self):
        return self._fork_builder()
     
    def build(self, *args, **kwargs):
        """Make object using forked builder with applied args, kwargs"""
        builder = self._fork_builder(*args, **kwargs)
        obj = builder._build_object()
        return obj
    
    @property
    def cls(self):
        return self._class
    
    @property
    def args(self):
        return self._args
    
    @property
    def kwargs(self):
        return self._kwargs
    
    @property
    def module(self):
        return self._module
    
    @property
    def updates(self):
        return self._updates
    
    #Protected
            
    def _fork_builder(self, *args, **kwargs):
        eargs = self._args+list(args)
        ekwargs = copy(self._kwargs)
        ekwargs.update(kwargs)
        ekwargs.setdefault('module', self._module)
        ekwargs.setdefault('updates', copy(self._updates))
        builder = type(self)(self._class, *eargs, **ekwargs)
        return builder
    
    def _build_object(self):
        obj = self._create_object()
        self._init_object(obj)
        return obj    
          
    def _create_object(self):
        return object.__new__(self._class)
        
    def _init_object(self, obj):
        obj.__meta_build__(self)
        if self._module != True:
            obj.__meta_init__(self._module)
    
    
def build(attribute, *args, **kwargs):
    return attribute.meta_builder.build(*args, **kwargs)