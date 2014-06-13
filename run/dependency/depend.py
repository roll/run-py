from .decorator import DependencyDecorator

class depend(DependencyDecorator):
    """Decorator to add custom dependency to method.
    
    Dependency has to be instance of :class:`run.dependency.Dependency`::
    
      class Module(Module):
    
          @depend(require('other_method'))
          @depend(custom_dependency)
          def method(self):
              pass
    """
    
    #Public
    
    def __init__(self, dependency):
        self._dep = dependency
    
    #Protected
    
    def _add_dependency(self, prototype):
        prototype.depend(self._dep)