from ..attribute import AttributeBuilder, AttributeBuilderCall

class TaskBuilder(AttributeBuilder):
    
    #Public
    
    def depend(self, *args, **kwargs):
        self._updates.append(self._call_class(
            'depend', *args, **kwargs))
        
    def require(self, *args, **kwargs):
        self._updates.append(self._call_class(
            'require', *args, **kwargs))
        
    def trigger(self, *args, **kwargs):
        self._updates.append(self._call_class(
            'trigger', *args, **kwargs))
        
    def ebable_dependency(self, *args, **kwargs):
        self._updates.append(self._call_class(
            'ebable_dependency', *args, **kwargs))
        
    def disable_dependency(self, *args, **kwargs):
        self._updates.append(self._call_class(
            'disable_dependency', *args, **kwargs))         
        
    #Protected
    
    _call_class = AttributeBuilderCall