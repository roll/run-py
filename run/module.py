import types
from abc import ABCMeta
from .field import Field
from .task import MethodTask

class ModuleMeta(ABCMeta):
   
    def __new__(cls, name, bases, attrs):
        for name, value in attrs.items():
            if not name.startswith('_'):
                #TODO: add other wrappings
                if isinstance(value, types.FunctionType):
                    attrs[name] = MethodTask(value)
        return super().__new__(cls, name, bases, attrs)


class Module(Field, metaclass=ModuleMeta):
    
    #Public
    
    def help(self, name=None):
        "Print field help"
        if name:
            prop = self._get_properties.get(name, None)
            if prop:
                print(prop.help())
        else:
            print('#Modules')               
            print('\n'.join(sorted(self._run_modules))) 
            print('#Tasks')               
            print('\n'.join(sorted(self._run_tasks)))
            print('#Vars')                       
            print('\n'.join(sorted(self._run_vars)))