from .builder import AttributeBuilder
from .update import AttributeSet

class AttributeDraft:

    #Public
    
    def __init__(self, cls, *args, **kwargs):
        builder = self._builder_class(cls, *args, **kwargs)
        super().__setattr__('_builder', builder)
    
    def __getattr__(self, name):
        try:
            return getattr(self._builder.cls, name)
        except AttributeError:
            raise AttributeError(                
                'AttributeDraft "{draft}" has no attribute "{name}"'.
                format(draft=self, name=name))
        
    def __setattr__(self, name, value):
        self._builder.updates.append(self._set_class(name, value))
        
    def __copy__(self):
        return self
      
    @property
    def meta_builder(self):
        return self._builder
        
    #Protected
    
    _builder_class = AttributeBuilder
    _set_class = AttributeSet        