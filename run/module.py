import types
from abc import ABCMeta
from .field import Field
from .task import MethodTask

class ModuleMeta(ABCMeta):
   
    #Public
   
    def __new__(cls, name, bases, attrs):
        for name, value in attrs.items():
            if not name.startswith('_'):
                #TODO: add other wrappings
                if isinstance(value, types.FunctionType):
                    attrs[name] = MethodTask(value)
        return super().__new__(cls, name, bases, attrs)


class Module(Field, metaclass=ModuleMeta):
    
    #Public
    
    def __get__(self, module, module_class=None):
        super().__get__(module, module_class)
        self._binding.resolve()        
        return self  
    
    def help(self, name=None):
        "Print field help"
        if name:
            prop = self._biding.fields.get(name, None)
            if prop:
                print(prop.help())
        else:
            print('#Modules')               
            print('\n'.join(sorted(self._biding.modules))) 
            print('#Tasks')               
            print('\n'.join(sorted(self._biding.tasks)))
            print('#Vars')                       
            print('\n'.join(sorted(self._biding.vars)))
            
            
class RunModule(Module):
    
    #Public
    
    pass            