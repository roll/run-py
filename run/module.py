from .namespace import Namespace
from .attribute import Attribute

class Module(Namespace,
             Attribute):
    
    #Public
    
    def __get__(self, namespace, namespace_class=None):
        return self
        
            
class RunModule(Module):
    
    #Public
    
    pass