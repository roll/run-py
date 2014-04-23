from abc import ABCMeta, abstractmethod

class DependencyResolver(metaclass=ABCMeta):

    #Public
    
    def bind(self, attribute):
        self._attribute = attribute 
        
    @abstractmethod
    def enable(self, task):
        pass #pragma: no cover
    
    @abstractmethod
    def disable(self, task):
        pass #pragma: no cover
    
    @abstractmethod    
    def resolve(self, attribute):
        pass #pragma: no cover
        
        
class DependencyCommonResolver(DependencyResolver):

    #Public
    
    def __init__(self, task, *args, **kwargs):
        self._task_name = task
        self._args = args
        self._kwargs = kwargs
        self._enabled = True
        
    def __repr__(self):
        result = repr(self._task)
        if self._args or self._kwargs:
            result += '('
            elements = []
            for arg in self._args:
                element = repr(arg)
                elements.append(element)
            for kwarg in self._kwargs.items():
                element = '{0}={1}'.format(*kwarg)
                elements.append(element)
            result += ', '.join(elements)
            result += ')'
        return result

    def enable(self, task):
        if task == self._task:
            self._enabled = True
    
    def disable(self, task):
        if task == self._task:
            self._enabled = False
    
    def resolve(self):
        self._task(*self._args, **self._kwargs)
        
    #Protected
    
    @property
    def _task(self):
        if self._attribute:
            task = getattr(self._attribute.meta_module, self._task_name)
            if not callable(task):
                raise TypeError(
                    'Attribute to depend upon "{task_name}" '
                    'must be a Task or a callable object.'.
                    format(task_name=self._task_name))
            return task            
        else:
            raise RuntimeError(
                'Dependency resolver "{resolver}" '
                'is not bound to any attribute'.
                format(resolver=self))
        
        
class DependencyNestedResolver(DependencyResolver):

    #Public
    
    def __init__(self, resolvers):
        self._resolvers = resolvers
        
    def __repr__(self):
        elements = []
        for resolver in self._resolvers:
            elements.append(repr(resolver))        
        return repr(elements)        
        
    def bind(self, attribute):
        for resolver in self._resolvers:
            resolver.bind(attribute)       

    def enable(self, task):
        for resolver in self._resolvers:
            resolver.enable(task)
    
    def disable(self, task):
        for resolver in self._resolvers:
            resolver.disable(task)
    
    def resolve(self):
        for resolver in self._resolvers:
            resolver.resolve()