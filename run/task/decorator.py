from abc import ABCMeta, abstractmethod
from ..dependent import DependentAttributeBuilder
from .method import MethodTask       

class TaskDecorator(metaclass=ABCMeta):
    
    #Public
    
    def __init__(self, tasks):
        self._tasks = tasks
    
    def __call__(self, method):
        if isinstance(method, self._builder_class):
            builder = method
        else:
            builder = MethodTask(method)
        self._add_dependency(builder)
        return builder
    
    #Protected
    
    _builder_class = DependentAttributeBuilder
    
    @abstractmethod
    def _add_dependency(self, builder):
        pass #pragma: no cover


class require(TaskDecorator):
    
    #Protected
    
    @abstractmethod
    def _add_dependency(self, builder):
        builder.require(self._tasks)


class trigger(TaskDecorator):
    
    #Protected
    
    @abstractmethod
    def _add_dependency(self, builder):
        builder.trigger(self._tasks)