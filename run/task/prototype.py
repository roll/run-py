from ..attribute import AttributePrototype, AttributeCall

class TaskPrototype(AttributePrototype):
    
    #Public
        
    def depend(self, *args, **kwargs):
        update = self._call_class('depend', *args, **kwargs)
        self._updates.append(update)
        return self
        
    def require(self, *args, **kwargs):
        update = self._call_class('require', *args, **kwargs)
        self._updates.append(update)
        return self 
        
    def trigger(self, *args, **kwargs):
        update = self._call_class('trigger', *args, **kwargs)
        self._updates.append(update)
        return self   
          
    def enable_dependency(self, *args, **kwargs):
        update = self._call_class('enable_dependency', *args, **kwargs)
        self._updates.append(update)
        return self  
        
    def disable_dependency(self, *args, **kwargs):
        update = self._call_class('disable_dependency', *args, **kwargs)
        self._updates.append(update)
        return self         
        
    #Protected
    
    _call_class = AttributeCall