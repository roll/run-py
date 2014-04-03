from .decorator import DependencyDecorator
from .dependency import Dependency

class require(DependencyDecorator, Dependency):
    
    #Public
    
    def resolve(self, is_fail=None):
        if is_fail == None:
            if not self._is_resolved:
                self._resolver.resolve()
                self._is_resolved = True
    
    #Protected
    
    def _add_dependency(self, prototype):
        prototype.depend(self)