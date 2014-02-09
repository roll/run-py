from copy import copy
from .update import AttributeBuilderSet

class AttributeBuilder:
    
    #Public
    
    def __init__(self, cls, *args, **kwargs):
        super().__setattr__('_class', cls)
        super().__setattr__('_args', args)
        super().__setattr__('_kwargs', kwargs)
        super().__setattr__('_updates', [])
        
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
    
    #Protected
    
    _set_class = AttributeBuilderSet
             
    def _create_object(self):
        return object.__new__(self._class)
        
    def _init_object(self, obj, *args, **kwargs):
        builder = self
        updates = copy(self._updates)
        eargs = self._args+args
        ekwargs = copy(self._kwargs)
        ekwargs.update(kwargs)
        module = ekwargs.pop('module', None)
        obj.__meta_build__(builder, updates, *eargs, **ekwargs)
        if module != True:
            obj.__meta_bind__(module)
            obj.__meta_init__()
            obj.__meta_update__()
            obj.__meta_ready__()