import inspect
from collections import OrderedDict
from abc import ABCMeta, abstractmethod
from .wrapper import Wrapper

class AttributeBuilder:
    
    #Public
    
    def __init__(self, cls, *args, **kwargs):
        self._class = cls
        self._args = args
        self._kwargs = kwargs
        
    def __call__(self):
        obj = self._make_object()
        self._sys_init_object(obj)
        return obj
    
    def __getattr__(self, name):
        try:
            #TODO: add some filters?
            return getattr(self._class, name)
        except:
            raise AttributeError(name) from None
    
    #Protected
    
    _sys_init_classes = property(lambda self: [Attribute])
    _sys_kwarg_keys = ['signature', 'docstring']
    
    def _sys_init_object(self, obj):
        sys_kwargs = self._make_sys_kwargs()
        for cls in self._sys_init_classes:
            cls.__init__(obj, **sys_kwargs)
    
    def _make_object(self):
        user_kwargs = self._make_user_kwargs()
        obj = object.__new__(self._class)
        obj.__init__(*self._args, **user_kwargs)
        return obj

    def _make_sys_kwargs(self):
        return {key: value for key, value in self._kwargs.items()
                if key in self._sys_kwarg_keys}

    def _make_user_kwargs(self):
        return {key: value for key, value in self._kwargs.items()
                if key not in self._sys_kwarg_keys}
        
        
class Attribute(metaclass=ABCMeta):
    
    #Public
    
    def __new__(cls, *args, **kwargs):
        builder = cls._builder_class(cls, *args, **kwargs)
        if 'module' not in kwargs:
            return builder
        else:
            return builder()
    
    def __init__(self, *args, **kwargs):
        self.__module = None
        self.__signature = kwargs.pop('signature', None)
        self.__docstring = kwargs.pop('docstring', None)
    
    @abstractmethod
    def __get__(self, module, module_class):
        pass #pragma: no cover
    
    def __set__(self, module, value):
        raise RuntimeError('Can\'t set attribute')
        
    @property
    def module(self):
        return self.__module
    
    @module.setter
    def module(self, module):
        self.__module = module
    
    @property
    def metadata(self):
        return AttributeMetadata(
            self, signature=self.__signature, 
                  docstring=self.__docstring)
        
    #Protected
    
    _builder_class = AttributeBuilder
        
  
class AttributeMetadata:
    
    #Public
    
    def __init__(self, attribute, signature=None, docstring=None):
        self._attribute = attribute
        self._signature = signature
        self._docstring = docstring

    @property
    def name(self):
        return '.'.join(filter(None, 
            [self.module_name, self.attribute_name]))
    
    @property
    def module_name(self):
        if self._attribute.module:
            return self._attribute.module.metadata.name 
        else:
            return ''  
    
    @property
    def attribute_name(self):
        if self._attribute.module:
            return (self._attribute.module.attributes.
                    find(self._attribute, default='')) 
        else:
            return '' 

    @property
    def help(self):
        return '\n'.join(filter(None, 
            [self.signature, self.docstring]))

    @property
    def signature(self):
        if self._signature:
            return self._signature
        else:
            return self.name    
    
    @property
    def docstring(self):
        if self._docstring:
            return self._docstring
        else:
            return inspect.getdoc(self._attribute)     


class DependentAttributeBuilder(AttributeBuilder):
    
    #Public
            
    def require(self, tasks, *args, **kwargs):
        self.__kwargs.setdefault('require', [])
        self.__kwargs['require'] += (tasks, args, kwargs)
        
    def trigger(self, tasks, *args, **kwargs):
        self.__kwargs.setdefault('trigger', [])
        self.__kwargs['require'] += (tasks, args, kwargs)
    
    #Protected

    @property
    def _sys_init_classes(self):
        return super()._sys_init_classes+[DependentAttribute]

    @property
    def _sys_kwarg_keys(self):
        return super()._sys_kwarg_keys+['require', 'trigger']
    
    
class DependentAttribute(Attribute):
    
    #Public
    
    def __init__(self, *args, **kwargs):
        self.__require = OrderedDict()
        self.__trigger = OrderedDict()
        self.__resolved_requirments = []
        self.require(kwargs.pop('require', []))
        self.trigger(kwargs.pop('trigger', []))
        
    def require(self, tasks, *args, **kwargs):
        self.__add_dependency(
            self.__require, tasks, *args, **kwargs)
        
    def trigger(self, tasks, *args, **kwargs):
        self.__add_dependency(
            self.__trigger, tasks, *args, **kwargs)
            
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
    
    @staticmethod
    def __add_dependency(target, tasks, *args, **kwargs):
        if not isinstance(tasks, list):
            tasks = [tasks] 
        for task in tasks:
            if isinstance(task, tuple):
                #TODO: add error handling
                kwargs = task[2]
                args = task[1]
                task = task[0]
            if task not in target:
                target[task] = DependentAttributeDependency(
                    task, *args, **kwargs)        
    
    
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
    
    def __init__(self, tasks, *args, **kwargs):
        self._tasks = tasks
        self._args = args
        self._kwargs = kwargs
    
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
        builder.require(self._tasks, self._args, self._kwargs)


class trigger(DependentAttributeDecorator):
    
    #Protected
    
    @abstractmethod
    def _add_dependency(self, builder):
        builder.trigger(self._tasks, self._args, self._kwargs)     