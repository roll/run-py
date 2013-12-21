from collections import OrderedDict
from abc import ABCMeta, abstractmethod
from .wrapper import Wrapper
from .attribute import Attribute, AttributeBuilder

class DependentAttributeBuilder(AttributeBuilder):
    
    #Public
    
    def require(self, *args, **kwargs):
        self._add_delayed_call('require', args, kwargs)
        
    def trigger(self, *args, **kwargs):
        self._add_delayed_call('trigger', args, kwargs)
    
    #Protected

    @property
    def _system_init_classes(self):
        return super()._system_init_classes+[DependentAttribute]

    @property
    def _system_kwarg_keys(self):
        return super()._system_kwarg_keys+['require', 'trigger']
    
    
class DependentAttribute(Attribute):
    
    #Public
    
    def __init__(self, *args, **kwargs):
        self._requirments = OrderedDict()
        self._triggers = OrderedDict()
        self._resolved_requirments = []
        self.require(kwargs.pop('require', []))
        self.trigger(kwargs.pop('trigger', []))
        
    def require(self, tasks, disable=False):
        self._update_dependencies(
            self._requirments, tasks, disable)
        
    def trigger(self, tasks, disable=False):
        self._update_dependencies(
            self._triggers, tasks, disable)
            
    #Protected
    
    _builder_class = DependentAttributeBuilder
            
    def _resolve_requirements(self):
        for task, dependency in self._requirments.items():
            if task not in self._resolved_requirments:
                dependency(self)
                self._resolved_requirments.append(task)
    
    def _process_triggers(self):
        for dependency in self._triggers.values():
            dependency(self)
            
    @classmethod
    def _update_dependencies(cls, target, tasks, disable=False):
        for task in tasks:
            if not disable:
                method = cls._add_dependency
            else:
                method = cls._remove_dependency
            method(target, task)
     
    #TODO: add error handling      
    #TODO: improve unpack logic
    @staticmethod 
    def _add_dependency(target, task):          
        args = []
        kwargs = {}
        if isinstance(task, tuple):
            args = task[1]
            kwargs = task[2]
            task = task[0]
        if task not in target:
            target[task] = DependentAttributeDependency(
                task, *args, **kwargs)
          
    @staticmethod            
    def _remove_dependency(target, task):          
        target.pop(task, None)
                        
    
class DependentAttributeDependency:
    
    #Public
    
    def __init__(self, task_name, *args, **kwargs):
        self._task_name = task_name
        self._args = args
        self._kwargs = kwargs
        
    def __call__(self, attribute):
        task = getattr(attribute.module, self._task_name)
        return task(*self._args, **self._kwargs)
    
    
class DependentAttributeDecorator(metaclass=ABCMeta):
    
    #Public
    
    def __init__(self, tasks):
        self._tasks = tasks
    
    def __call__(self, method):
        wrapper = Wrapper()
        if isinstance(method, AttributeBuilder):
            builder = method
        else:
            builder = wrapper.wrap_method(method)
        self._add_dependency(builder)
        return builder
    
    #Protected
    
    @abstractmethod
    def _add_dependency(self, builder):
        pass #pragma: no cover


class require(DependentAttributeDecorator):
    
    #Protected
    
    @abstractmethod
    def _add_dependency(self, builder):
        builder.require(self._tasks)


class trigger(DependentAttributeDecorator):
    
    #Protected
    
    @abstractmethod
    def _add_dependency(self, builder):
        builder.trigger(self._tasks)