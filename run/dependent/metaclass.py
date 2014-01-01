from ..attribute import AttributeMetaclass
from .builder import DependentAttributeBuilder

class DependentAttributeMetaclass(AttributeMetaclass):
    
    #Protected
    
    _builder_class = DependentAttributeBuilder