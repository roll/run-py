from collections import OrderedDict
from abc import ABCMeta, abstractmethod
from .wrapper import Wrapper
from .attribute import Attribute, AttributeBuilder

class DependentAttributeBuilder(AttributeBuilder):
    
    #Public
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__delayed_calls = []
    
    def require(self, *args, **kwargs):
        self.__delayed_calls.append(('require', args, kwargs))
        
    def trigger(self, *args, **kwargs):
        self.__delayed_calls.append(('trigger', args, kwargs))
    
    #Protected

    @property
    def _sys_init_classes(self):
        return super()._sys_init_classes+[DependentAttribute]

    @property
    def _sys_kwarg_keys(self):
        return super()._sys_kwarg_keys+['require', 'trigger']
     
    #TODO: add error handling      
    #TODO: improve unpack logic
    def _sys_init_object(self, obj):
        super()._sys_init_object(obj)
        for call in self.__delayed_calls:
            method = getattr(obj, call[0])
            method(*call[1], **call[2])
    
    
class DependentAttribute(Attribute):
    
    #Public
    
    def __init__(self, *args, **kwargs):
        self.__require = OrderedDict()
        self.__trigger = OrderedDict()
        self.__resolved_requirments = []
        self.require(kwargs.pop('require', []))
        self.trigger(kwargs.pop('trigger', []))
        
    def require(self, tasks, disable=False):
        self.__update_dependencies(
            self.__require, tasks, disable)
        
    def trigger(self, tasks, disable=False):
        self.__update_dependencies(
            self.__trigger, tasks, disable)
            
    def resolve_requirements(self):
        for task, dependency in self.__require.items():
            if task not in self.__resolved_requirments:
                dependency(self)
                self.__resolved_requirments.append(task)
    
    def process_triggers(self):
        for dependency in self.__trigger.values():
            dependency(self)
            
    #Protected
    
    _builder_class = DependentAttributeBuilder
    
    #Private
    
    @classmethod
    def __update_dependencies(cls, target, tasks, disable=False):
        for task in tasks:
            if not disable:
                method = cls.__add_dependency
            else:
                method = cls.__remove_dependency
            method(target, task)
     
    #TODO: add error handling      
    #TODO: improve unpack logic
    @staticmethod 
    def __add_dependency(target, task):          
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
    def __remove_dependency(target, task):          
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