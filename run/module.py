import types
from abc import ABCMeta
from functools import wraps
from .property import Property
from .task import MethodTask

class ModuleMeta(ABCMeta):
   
    def __new__(cls, name, bases, attrs):
        for name, value in attrs.items():
            #TODO: add plain vars wrapping?
            if isinstance(value, types.FunctionType):
                attrs[name] = MethodTask(value)
        return super().__new__(cls, name, bases, attrs)


class Module(Property, metaclass=ModuleMeta):
    
    #Public
    
    def __get__(self, run, runclass=None):
        self._run = run
        return self
    
    def help(self, name=None):
        "Print property help"
        if not name:
            print('#Tasks')               
            print('\n'.join(sorted(self._tasks)))
            print('#Vars')                       
            print('\n'.join(sorted(self._vars)))
        else:       
            property = self._get_properties().get(name, None)
            if property:
                print(property.help())
            
    #Protected
    
    def _get_properties(self, subclass=None):
        properties = {}
        for cls in self.__class__.mro():
            for name, attr in cls.__dict__.items():
                if isinstance(attr, Property):
                    if not subclass or isinstance(attr, subclass):
                        properties[name] = attr
        return properties
    

def require(tasks):
    @wraps
    def wrapper(method):
        return MethodTask(method, require=tasks)
    return wrapper