from .decorator import DependencyDecorator

class depend(DependencyDecorator):
    """Decorate method to add custom dependency.
    
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