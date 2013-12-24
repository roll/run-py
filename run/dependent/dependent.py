from collections import OrderedDict
from ..attribute import AttributeMetaclass, Attribute
from .builder import DependentAttributeBuilder
from .task import DependentAttributeTask

class DependentAttributeMetaclass(AttributeMetaclass):
    
    #Protected
    
    _builder_class = DependentAttributeBuilder
    
    
class DependentAttribute(Attribute, metaclass=DependentAttributeMetaclass):
    
    #Public
    
    def __meta_init__(self, args, kwargs):
        super().__meta_init__(args, kwargs)
        self._requirments = OrderedDict()
        self._triggers = OrderedDict()
        self.require(kwargs.pop('require', []))
        self.trigger(kwargs.pop('trigger', []))
        
    def require(self, tasks, disable=False):
        self._update_tasks(self._requirments, tasks, disable)
        
    def trigger(self, tasks, disable=False):
        self._update_tasks(self._triggers, tasks, disable)
            
    #Protected
            
    def _resolve_requirements(self):
        for task in self._requirments.values():
            if not task.is_executed:
                task(self)
    
    def _process_triggers(self):
        for task in self._triggers.values():
            task(self)
            
    @classmethod
    def _update_tasks(cls, group, tasks, disable=False):
        for task in tasks:
            task = DependentAttributeTask(task)
            if disable:
                group.pop(task.name, None)
            else:
                if task.name not in group:
                    group[task.name] = task