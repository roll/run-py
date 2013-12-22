from collections import OrderedDict
from abc import ABCMeta, abstractmethod
from .wrapper import Wrapper
from .attribute import (AttributeBuilder, AttributeBuilderCall, 
                        AttributeMeta, Attribute)

class DependentAttributeBuilder(AttributeBuilder):
    
    #Public
    
    def require(self, *args, **kwargs):
        self._updates.append(
            AttributeBuilderCall('require', *args, **kwargs))
        
    def trigger(self, *args, **kwargs):
        self._updates.append(
            AttributeBuilderCall('trigger', *args, **kwargs))
    
    
class DependentAttributeMeta(AttributeMeta):
    
    #Protected
    
    _builder_class = DependentAttributeBuilder 
    
    
class DependentAttribute(Attribute, metaclass=DependentAttributeMeta):
    
    #Public
    
    def __system_init__(self, args, kwargs):
        super().__system_init__(args, kwargs)
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
                     
    
class DependentAttributeTask:
    
    #Public
    
    def __init__(self, task):
        self._unpack(task)
        self._is_executed = False
        
    def __call__(self, attribute):
        task = getattr(attribute.module, self.name)
        result = task(*self.args, **self.kwargs)
        self._is_executed = True
        return result
    
    @property
    def name(self):
        return self._name
    
    @property
    def args(self):
        return self._args
    
    @property
    def kwargs(self):
        return self._kwargs
    
    @property
    def is_executed(self):
        return self._is_executed
    
    #Protected
    
    def _unpack(self, task):
        self._name = ''
        self._args = []
        self._kwargs = {}
        if isinstance(task, tuple):
            try:
                self._name = task[0]
                self._args = task[1]
                self._kwargs = task[2]
            except IndexError:
                pass
        else:
            self._name = task      
    
    
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