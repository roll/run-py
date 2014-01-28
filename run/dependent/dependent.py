from collections import OrderedDict
from ..attribute import Attribute
from .dependency import DependentAttributeDependency
from .metaclass import DependentAttributeMetaclass
    
class DependentAttribute(Attribute, metaclass=DependentAttributeMetaclass):
    
    #Public
    
    def __meta_init__(self, args, kwargs):
        super().__meta_init__(args, kwargs)
        self._requirments = OrderedDict()
        self._triggers = OrderedDict()
        self.require(kwargs.pop('require', []))
        self.trigger(kwargs.pop('trigger', []))
        
    def require(self, tasks, disable=False):
        self._update_dependencies(self._requirments, tasks, disable)
        
    def trigger(self, tasks, disable=False):
        self._update_dependencies(self._triggers, tasks, disable)
            
    #Protected
    
    _dependency_class = DependentAttributeDependency
            
    def _resolve_requirements(self):
        for dependency in self._requirments.values():
            if dependency.is_resolved:
                continue
            dependency.resolve(self)
    
    def _resolve_triggers(self):
        for dependency in self._triggers.values():
            dependency.resolve(self)
            
    @classmethod
    def _update_dependencies(cls, group, tasks, disable=False):
        for task in tasks:
            dependency = cls._dependency_class(task)
            if disable:
                group.pop(dependency.name, None)
            else:
                if dependency.name not in group:
                    group[dependency.name] = dependency