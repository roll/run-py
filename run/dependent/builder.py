from ..attribute import AttributeBuilder, AttributeBuilderCall

class DependentAttributeBuilder(AttributeBuilder):
    
    #Public
    
    def require(self, *args, **kwargs):
        self._updates.append(
            AttributeBuilderCall('require', *args, **kwargs))
        
    def trigger(self, *args, **kwargs):
        self._updates.append(
            AttributeBuilderCall('trigger', *args, **kwargs))