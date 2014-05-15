from .decorator import DependencyDecorator
from .dependency import Dependency

class trigger(DependencyDecorator, Dependency):
    
    #Public
    
    def __init__(self, task, *args, **kwargs):
        self._on_success = kwargs.pop('on_success', True)
        self._on_fail = kwargs.pop('on_fail', False)          
        super().__init__(task, *args, **kwargs)

     
    def resolve(self, failed=None):
        if failed != None:
            if (self._on_success and not failed or
                self._on_fail and failed):
                self._resolver.resolve()
    
    #Protected
    
    def _add_dependency(self, prototype):
        prototype.depend(self)