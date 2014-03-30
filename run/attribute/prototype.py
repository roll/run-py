from copy import copy
from .update import AttributeSet

class AttributePrototype:

    #Public
    
    def __init__(self, cls, *args, **kwargs):
        super().__setattr__('_module', kwargs.pop('module', None))
        super().__setattr__('_updates', kwargs.pop('updates', []))
        super().__setattr__('_class', cls)
        super().__setattr__('_args', list(args))
        super().__setattr__('_kwargs', kwargs)        
    
    def __getattr__(self, name):
        try:
            return getattr(self._class, name)
        except AttributeError:
            raise AttributeError(                
                'AttributePrototype "{prototype}" has no attribute "{name}"'.
                format(prototype=self, name=name))
        
    def __setattr__(self, name, value):
        self._updates.append(self._set_class(name, value))
     
    def __call__(self, **kwargs):
        """Create attribute"""
        #TODO: temporary fix
        self._kwargs.update(kwargs)
        attribute = self._create_attribute()
        self._init_attribute(attribute)
        return attribute
        
    def __copy__(self):
        """Copy prototype"""
        return type(self)(
            self._class, *self._args, module=self._module, 
            updates=copy(self._updates), **self._kwargs)
     
    #Protected
    
    _set_class = AttributeSet
          
    def _create_attribute(self):
        return object.__new__(self._class)
        
    def _init_attribute(self, attribute):
        kwargs = copy(self._kwargs)
        kwargs.setdefault('updates', copy(self._updates))        
        attribute.__meta_build__(*self._args, **kwargs)
        if self._module != True:
            attribute.__meta_init__(self._module)