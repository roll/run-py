from .decorator import DependencyDecorator
from .dependency import Dependency

class require(DependencyDecorator, Dependency):
    """Decorate method to add require dependency.
    
    Usage example::
    
      class Module(Module):
    
          @require('other_method')
          def method(self):
              pass
    
    It's a shortcut for :class:`run.dependency.depend` decorator.
    """    
    
    #Public
    
    def resolve(self, failed=None):
        if failed == None:
            if not self._is_resolved:
                self._resolver.resolve()
                self._is_resolved = True
    
    #Protected
    
    def _add_dependency(self, prototype):
        prototype.depend(self)