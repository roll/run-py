from .namespace import NamespaceMixin
from .attribute import AttributeMixin

class Module(NamespaceMixin,
             AttributeMixin):
    
    #Public
    
    def help(self, name=None):
        "Print field help"
        if name:
            prop = self['module_fields'].get(name, None)
            if prop:
                print(prop.help())
        else:
            print('#Modules')               
            print('\n'.join(sorted(self['modules']))) 
            print('#Tasks')               
            print('\n'.join(sorted(self['tasks'])))
            print('#Vars')                       
            print('\n'.join(sorted(self['vars'])))
            
            
class RunModule(Module):
    
    #Public
    
    pass        


