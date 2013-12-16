from .namespace import NamespaceMixin
from .attribute import AttributeMixin
from .unit import Unit

class Module(NamespaceMixin,
             AttributeMixin,
             Unit):
    
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