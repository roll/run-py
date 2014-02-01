from abc import ABCMeta, abstractmethod
from .builder import TaskBuilder
from .method import MethodTask       

class TaskDependency(metaclass=ABCMeta):
    
    #Public
    
    def __init__(self, task, *args, **kwargs):
        self._components = []
        if not isinstance(task, list):
            dependencies = [task]
        else:
            dependencies = task
        for dependency in dependencies:
            component = TaskDependencyComponent(dependency)
            self._components.append(component)
        self._args = args
        self._kwargs = kwargs
        self._is_resolved = False
    
    def __call__(self, method):
        if not isinstance(method, self._builder_class):
            builder = self._method_task_class(method)
        else:
            builder = method
        self._apply_dependency(builder)
        return builder
    
    def enable(self, task):
        for component in self._components:
            component.enable(task)
    
    def disable(self, task):
        for component in self._components:
            component.disable(task)
        
    def resolve(self, attribute):
        for component in self._components:
            component.resolve(attribute)
        self._is_resolved = True

    @property
    def is_resolved(self):
        return self._is_resolved
    
    #Protected
    
    _builder_class = TaskBuilder
    _method_task_class = MethodTask
    
    @abstractmethod
    def _apply_dependency(self, builder):
        pass #pragma: no cover
        

class TaskDependencyComponent:
    
    #Public
    
    def __init__(self, dependency):
        self._dependency = dependency
        self._enabled = True
        
    def enable(self, task):
        if isinstance(self._dependency, TaskDependency):
            self._dependency.enable(task)
        else:
            self._enabled = True
    
    def disable(self, task):
        if isinstance(self._dependency, TaskDependency):
            self._dependency.disable(task)
        else:
            self._enabled = False
        
    def resolve(self, attribute):
        if self._enabled:
            if isinstance(self._dependency, TaskDependency):
                self._dependency.resolve(attribute)
            else:
                task = getattr(attribute.meta_module, self._dependency)
                task(*self._args, **self._kwargs)
    
    
class require(TaskDependency):
    
    #Protected
    
    def _apply_dependency(self, builder):
        builder.require(self)


class trigger(TaskDependency):
    
    #Protected
    
    def _apply_dependency(self, builder):
        builder.trigger(self)