from ..attribute import AttributeMetaclass
from .draft import TaskDraft

class TaskMetaclass(AttributeMetaclass):
    
    #Protected
    
    _draft_class = TaskDraft