from ..attribute import AttributeDraft, AttributeCall

class TaskDraft(AttributeDraft):
    
    #Public
        
    def depend(self, *args, **kwargs):
        update = self._call_class('depend', *args, **kwargs)
        self._builder.updates.append(update)
        
    def require(self, *args, **kwargs):
        update = self._call_class('require', *args, **kwargs)
        self._builder.updates.append(update)        
        
    def trigger(self, *args, **kwargs):
        update = self._call_class('trigger', *args, **kwargs)
        self._builder.updates.append(update)        
    
    def add_dependency(self, *args, **kwargs):
        update = self._call_class('add_dependency', *args, **kwargs)
        self._builder.updates.append(update)        
          
    def enable_dependency(self, *args, **kwargs):
        update = self._call_class('enable_dependency', *args, **kwargs)
        self._builder.updates.append(update)        
        
    def disable_dependency(self, *args, **kwargs):
        update = self._call_class('disable_dependency', *args, **kwargs)
        self._builder.updates.append(update)          
        
    #Protected
    
    _call_class = AttributeCall