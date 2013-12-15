from .namespace import NamespaceMixin
from .attribute import AttributeMixin

class Module(NamespaceMixin,
             AttributeMixin):
    
    #Public
    
    def help(self, name=None):
        "Print help"
        #For help
        #print(self._parser.format_help().strip())
        #sys.exit()
        if name:
            prop = self.attributes.get(name, None)
            if prop:
                print(prop.help())
        else:
            print('\n'.join(sorted(self.attributes))) 
            
            
class RunModule(Module):
    
    #Public
    
    pass