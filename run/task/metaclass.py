from ..attribute import AttributeMetaclass
from .builder import TaskBuilder

class TaskMetaclass(AttributeMetaclass):
    
    #Protected
    
    _builder_class = TaskBuilder