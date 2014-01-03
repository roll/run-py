from abc import ABCMeta, abstractmethod
from ..dependent import DependentAttributeBuilder
from .function import FunctionTask       

class TaskDecorator(metaclass=ABCMeta):
    
    #Public
    
    def __init__(self, tasks):
        self._tasks = tasks
    
    def __call__(self, function):
        if isinstance(function, self._builder_class):
            builder = function
        else:
            builder = self._attribute_class(function)
        self._add_dependency(builder)
        return builder
    
    #Protected
    
    _builder_class = DependentAttributeBuilder
    _attribute_class = FunctionTask
    
    @abstractmethod
    def _add_dependency(self, builder):
        pass #pragma: no cover


class require(TaskDecorator):
    
    #Protected
    
    def _add_dependency(self, builder):
        builder.require(self._tasks)


class trigger(TaskDecorator):
    
    #Protected
    
    def _add_dependency(self, builder):
        builder.trigger(self._tasks)