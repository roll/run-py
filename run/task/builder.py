from ..attribute import AttributeBuilder, AttributeBuilderCall

class TaskBuilder(AttributeBuilder):
    
    #Public
    
    def require(self, *args, **kwargs):
        self._updates.append(self._call_class('require', *args, **kwargs))
        
    def trigger(self, *args, **kwargs):
        self._updates.append(self._call_class('trigger', *args, **kwargs))
        
    #Protected
    
    _call_class = AttributeBuilderCall