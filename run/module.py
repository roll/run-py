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


class Module(metaclass=ModuleMeta):
    
    #Public
    
    #TODO: add list of vars
    def list(self):
        "Print list of tasks/vars"
        print('#Tasks')               
        print('\n'.join(sorted(self._tasks)))
        print('#Vars')                       
        print('\n'.join(sorted(self._vars)))
    
    def help(self, name):
        "Print task/var help"        
        attr = self._tasks.get(name, None) or self._vars.get(name, None)
        if attr:
            print(attr.help())
        else:
            print('No name "{0}"'.format(name))
            
    #Protected
    
    def _get_properties(self, subclass=None):
        properties = {}
        for cls in self.__class__.mro():
            for name, attr in cls.__dict__.items():
                if isinstance(attr, Property):
                    if not subclass or isinstance(attr, subclass):
                        properties[name] = attr
        return properties
    

def require(*task_names):
    @wraps
    def wrapper(method):
        return MethodTask(method, require=task_names)
    return wrapper