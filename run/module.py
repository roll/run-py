import types
from abc import ABCMeta
from functools import wraps
from .property import Property
from .task import Task, MethodTask
from .var import Var

class ModuleMeta(ABCMeta):
   
    def __new__(cls, name, bases, attrs):
        for name, value in attrs.items():
            if not name.startswith('_'):
                #TODO: add other wrappings
                if isinstance(value, types.FunctionType):
                    attrs[name] = MethodTask(value)
        return super().__new__(cls, name, bases, attrs)


class Module(Property, metaclass=ModuleMeta):
    
    #Public
    
    def help(self, name=None):
        "Print property help"
        if name:
            property = self._get_properties().get(name, None)
            if property:
                print(property.help())
        else:
            modules = self._get_properties(type=Module)
            tasks = self._get_properties(type=Task)
            vars = self._get_properties(type=Var)       
            print('#Modules')               
            print('\n'.join(sorted(modules)))
            print('#Tasks')               
            print('\n'.join(sorted(tasks)))
            print('#Vars')                       
            print('\n'.join(sorted(vars)))                
            
    #Protected
    
    def _get_properties(self, type=None):
        properties = {}
        for cls in self.__class__.mro():
            for name, attr in cls.__dict__.items():
                if isinstance(attr, Property):
                    if not type or isinstance(attr, type):
                        properties[name] = attr
        return properties
    

def require(tasks):
    @wraps
    def wrapper(method):
        return MethodTask(method, require=tasks)
    return wrapper