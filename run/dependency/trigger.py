from .dependency import Dependency

class trigger(Dependency):
    
    #Public
    
    @property
    def is_resolved(self):
        return False
    
    #Protected
    
    def _add_dependency(self, builder):
        builder.trigger(self)