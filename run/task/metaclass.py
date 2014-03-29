from ..attribute import AttributeMetaclass
from .prototype import TaskPrototype

class TaskMetaclass(AttributeMetaclass):
    
    #Protected
    
    _prototype_class = TaskPrototype