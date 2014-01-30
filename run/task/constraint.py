from abc import ABCMeta, abstractmethod
from .builder import TaskBuilder
from .method import MethodTask       

class TaskConstraint(metaclass=ABCMeta):
    
    #Public
    
    def __init__(self, tasks):
        self._tasks = tasks
    
    def __call__(self, method):
        if isinstance(method, self._builder_class):
            builder = method
        else:
            builder = self._attribute_class(method)
        self._apply_dependency(builder)
        return builder
    
    #Protected
    
    _builder_class = TaskBuilder
    _attribute_class = MethodTask
    
    @abstractmethod
    def _apply_dependency(self, builder):
        pass #pragma: no cover


class require(TaskConstraint):
    
    #Protected
    
    def _apply_dependency(self, builder):
        builder.require(self._tasks)


class trigger(TaskConstraint):
    
    #Protected
    
    def _apply_dependency(self, builder):
        builder.trigger(self._tasks)