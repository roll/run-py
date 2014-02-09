from copy import copy
from .update import AttributeBuilderSet

class AttributeBuilder:
    
    #Public
    
    def __init__(self, cls, *args, **kwargs):
        module = kwargs.pop('module', None)
        updates = kwargs.pop('updates', [])
        super().__setattr__('_class', cls)
        super().__setattr__('_args', list(args))
        super().__setattr__('_kwargs', kwargs)
        super().__setattr__('_module', module)
        super().__setattr__('_updates', updates)
        
    def __call__(self, *args, **kwargs):
        obj = self._create_object()
        self._init_object(obj, *args, **kwargs)
        return obj
    
    def __getattr__(self, name):
        try:
            return getattr(self._class, name)
        except AttributeError:
            raise AttributeError(                
                'Builder "{builder}" has no attribute "{name}"'.
                format(builder=self, name=name))
        
    def __setattr__(self, name, value):
        self._updates.append(self._set_class(name, value))
    
    @property
    def meta_class(self):
        return self._class
    
    @property
    def meta_args(self):
        return self._args
    
    @property
    def meta_kwargs(self):
        return self._kwargs
    
    @property
    def meta_module(self):
        return self._module 
    
    @property
    def meta_updates(self):
        return self._updates        
    
    #Protected
    
    _set_class = AttributeBuilderSet
             
    def _create_object(self):
        return object.__new__(self._class)
        
    def _init_object(self, obj, *args, **kwargs):
        builder = self._fork_builder(*args, **kwargs)
        obj.__meta_build__(builder)
        if builder.meta_module != True:
            obj.__meta_bind__(builder.meta_module)
            obj.__meta_init__()
            obj.__meta_update__()
            obj.__meta_ready__()
            
    def _fork_builder(self, *args, **kwargs):
        eargs = self._args+list(args)
        ekwargs = copy(self._kwargs)
        ekwargs.update(kwargs)
        ekwargs.setdefault('module', self._module)
        ekwargs.setdefault('updates', copy(self._updates))
        builder = type(self)(self._class, *eargs, **ekwargs)
        return builder