__all__ = ['AttributeBuilder']

from .update import AttributeBuilderSet

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
        self._updates.append(AttributeBuilderSet(name, value))     
    
    #Protected
             
    def _create_object(self):
        return object.__new__(self._class)
        
    def _init_object(self, obj):
        obj.__system_init__(self._args, self._kwargs)
        obj.__init__(*self._args, **self._kwargs)
     
    def _update_object(self, obj):
        for update in self._updates:
            update.apply(obj)