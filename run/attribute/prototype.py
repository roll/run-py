from copy import copy
from .update import AttributeSet, AttributeCall

#TODO: add _getattr state check
class AttributePrototype:

    #Public
    
    __isabstractmethod__ = False
    __isskippedmethod__ = False
    
    def __init__(self, cls, updates, *args, **kwargs):
        super().__setattr__('_class', cls)
        super().__setattr__('_updates', updates)        
        super().__setattr__('_args', args)
        super().__setattr__('_kwargs', kwargs)
        super().__setattr__('_getattr', None) 
        if self._updates == None:
            super().__setattr__('_updates', [])
            
    def __getattr__(self, name):
        try: 
            return getattr(self._class, name)
        except AttributeError:
            super().__setattr__('_getattr', name)
            return self
        
    def __setattr__(self, name, value):
        update = self._set_class(name, value)
        self._updates.append(update)
    
    def __call__(self, *args, **kwargs):
        update = self._call_class(self._getattr, *args, **kwargs)
        super().__setattr__('_getattr', None)
        self._updates.append(update)
        return self
        
    def __copy__(self):
        """Copy prototype"""
        return type(self)(
            self._class, copy(self._updates), 
            *self._args, **self._kwargs)
    
    def __build__(self, module):
        """Build attribute"""
        attribute = self._create_attribute()
        self._init_attribute(attribute, module)
        self._update_attribute(attribute)
        return attribute        
     
    #Protected
    
    _set_class = AttributeSet
    _call_class = AttributeCall
          
    def _create_attribute(self):
        return object.__new__(self._class)
        
    def _init_attribute(self, attribute, module):
        attribute.__meta_init__(module, *self._args, **self._kwargs)
        
    def _update_attribute(self, attribute):
        for update in self._updates:
            update.apply(attribute)