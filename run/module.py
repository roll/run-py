from .namespace import Namespace
from .attribute import Attribute

class Module(Namespace,
             Attribute):
    
    #Public
    
    @property
    def unit_name(self):
        pass
    
    @property
    def unit_help(self):
        pass
        
            
class RunModule(Module):
    
    #Public
    
    pass