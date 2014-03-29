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
     
    def __call__(self, *args, **kwargs):
        """Build object using forked prototype with applied args, kwargs"""
        prototype = self._fork_prototype(*args, **kwargs)
        obj = prototype._build_attribute()
        return obj
        
    def __copy__(self):
        return self._fork_prototype()
      
    @property
    def meta_prototype(self):
        return self
     
    #Protected
    
    _set_class = AttributeSet
    
    def _fork_prototype(self, *args, **kwargs):
        eargs = self._args+list(args)
        ekwargs = copy(self._kwargs)
        ekwargs.update(kwargs)
        ekwargs.setdefault('module', self._module)
        ekwargs.setdefault('updates', copy(self._updates))
        prototype = type(self)(self._class, *eargs, **ekwargs)
        return prototype
    
    def _build_attribute(self):
        attribute = self._create_attribute()
        self._init_attribute(attribute)
        return attribute    
          
    def _create_attribute(self):
        return object.__new__(self._class)
        
    def _init_attribute(self, attribute):
        kwargs = copy(self._kwargs)
        kwargs.setdefault('updates', copy(self._updates))        
        attribute.__meta_build__(self, *self._args, **kwargs)
        if self._module != True:
            attribute.__meta_init__(self._module)  
            
            
def build(attribute, *args, **kwargs):
    return attribute.meta_prototype(*args, **kwargs)  