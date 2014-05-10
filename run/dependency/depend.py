from .decorator import DependencyDecorator

class depend(DependencyDecorator):
    
    #Public
    
    def __init__(self, dependency):
        self._dep = dependency
    
    #Protected
    
    def _add_dependency(self, prototype):
        prototype.depend(self._dep)