from abc import ABCMeta, abstractmethod
from box.importlib import import_object
from ..attribute import AttributePrototype

class DependencyDecorator(metaclass=ABCMeta):
    
    #Public    
    
    def __call__(self, method):
        prototype = method
        if not isinstance(method, AttributePrototype):
            prototype = self._method_task_class(method)
        self._add_dependency(prototype)
        return prototype
    
    #Protected    
    
    @property
    def _method_task_class(self):
        from ..task import MethodTask
        return MethodTask
    
    @abstractmethod
    def _add_dependency(self, prototype):
        pass #pragma: no cover
        
        
class depend(DependencyDecorator):
    
    #Public
    
    def __init__(self, dependency):
        self._dep = dependency
    
    #Protected
    
    def _add_dependency(self, prototype):
        prototype.depend(self._dep)