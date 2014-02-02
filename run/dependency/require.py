from .dependency import Dependency

class require(Dependency):
    
    #Public
    
    @property
    def is_resolved(self):
        return bool(self._resolves)    
    
    #Protected
    
    def _add_dependency(self, builder):
        builder.require(self)