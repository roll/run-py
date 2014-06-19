import inspect
from copy import copy
from .update import AttributeSet, AttributeCall

class AttributePrototype:

    #Public
    
    def __init__(self, cls, updates, *args, **kwargs):
        super().__setattr__('_class', cls)
        super().__setattr__('_updates', updates)        
        super().__setattr__('_args', args)
        super().__setattr__('_kwargs', kwargs)
        super().__setattr__('_getattr', None) 
        if self._updates == None:
            super().__setattr__('_updates', [])
            
    #TODO: add _getattr state check            
    def __getattr__(self, name):
        if name.startswith('_'):
            return super().__getattr__(name)
        if hasattr(self._class, name):
            attr = getattr(self._class, name)
            if not inspect.isfunction(attr):
                return attr
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
        
    def __copy__(self, *args, **kwargs):
        #Documented public wrapper is :func:`run.attribute.fork`
        eupdates = copy(self._updates)
        eargs = self._args+args
        ekwargs = self._kwargs
        ekwargs.update(kwargs)
        return type(self)(self._class, eupdates, *eargs, **ekwargs)
    
    def __build__(self, module):
        #Documented public wrapper is :func:`run.attribute.build`
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
        attribute.__build__(module, *self._args, **self._kwargs)
        
    def _update_attribute(self, attribute):
        for update in self._updates:
            update.apply(attribute)