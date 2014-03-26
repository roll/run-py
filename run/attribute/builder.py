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
        return self.fork()
            
    def fork(self, *args, **kwargs):
        eargs = self._args+list(args)
        ekwargs = copy(self._kwargs)
        ekwargs.update(kwargs)
        ekwargs.setdefault('module', self._module)
        ekwargs.setdefault('updates', copy(self._updates))
        builder = type(self)(self._class, *eargs, **ekwargs)
        return builder
     
    def build(self, *args, **kwargs):
        obj = self._create_object()
        self._init_object(obj, *args, **kwargs)
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
             
    def _create_object(self):
        return object.__new__(self._class)
        
    def _init_object(self, obj, *args, **kwargs):
        builder = self.fork(*args, **kwargs)
        obj.__meta_build__(builder)
        if builder.module != True:
            obj.__meta_bind__(builder.module)
            obj.__meta_init__()
            obj.__meta_update__()
            obj.__meta_ready__()
    
    
def build(attribute, *args, **kwargs):
    return attribute.meta_builder.build(*args, **kwargs)