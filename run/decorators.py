from abc import ABCMeta, abstractmethod
from .attribute import AttributeBuilder 
from .wrapper import Wrapper

class DependencyDecorator(metaclass=ABCMeta):
    
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


class require(DependencyDecorator):
    
    #Protected
    
    @abstractmethod
    def _add_dependency(self, builder):
        builder.require(self._tasks, self._args, self._kwargs)


class trigger(DependencyDecorator):
    
    #Protected
    
    @abstractmethod
    def _add_dependency(self, builder):
        builder.trigger(self._tasks, self._args, self._kwargs)  