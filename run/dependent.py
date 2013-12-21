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
        self._update_callbacks(self._requirments, tasks, disable)
        
    def trigger(self, tasks, disable=False):
        self._update_callbacks(self._triggers, tasks, disable)
            
    #Protected
    
    _builder_class = DependentAttributeBuilder
            
    def _resolve_requirements(self):
        for name, callback in self._requirments.items():
            if name not in self._resolved_requirments:
                callback(self)
                self._resolved_requirments.append(name)
    
    def _process_triggers(self):
        for callback in self._triggers.values():
            callback(self)
            
    @classmethod
    def _update_callbacks(cls, callbacks, tasks, disable=False):
        for task in tasks:
            callback = DependentAttributeCallback(task)
            if disable:
                callbacks.pop(callback.name, None)
            else:
                if callback.name not in callbacks:
                    callbacks[callback.name] = callback   
                     
    
class DependentAttributeCallback:
    
    #Public
    
    def __init__(self, task):
        self._unpack(task)
        
    def __call__(self, attribute):
        task = getattr(attribute.module, self.name)
        return task(*self.args, **self.kwargs)
    
    @property
    def name(self):
        return self._name
    
    @property
    def args(self):
        return self._args
    
    @property
    def kwargs(self):
        return self._kwargs
    
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