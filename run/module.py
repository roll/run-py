import types
from abc import ABCMeta
from .field import Field
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


class Module(Field, metaclass=ModuleMeta):
    
    #Public
    
    def help(self, name=None):
        "Print property help"
        if name:
            prop = self._get_properties.get(name, None)
            if prop:
                print(prop.help())
        else:
            modules = [name for name, prop in self._properties.items() 
                       if isinstance(prop, Module)]
            tasks = [name for name, prop in self._properties.items()
                     if isinstance(prop, Task)]
            vars = [name for name, prop in self._properties.items()
                    if isinstance(prop, Var)]       
            if modules:
                print('#Modules')               
                print('\n'.join(sorted(modules))) 
            if tasks:
                print('#Tasks')               
                print('\n'.join(sorted(tasks)))
            if vars:
                print('#Vars')                       
                print('\n'.join(sorted(vars)))
            
    #Protected
    
    @property
    def _properties(self):
        properties = {}
        for cls in self.__class__.mro():
            for name, attr in cls.__dict__.items():
                if isinstance(attr, Field):
                    properties[name] = attr
        return properties
             
    @property
    def _run(self):
        try:
            return self._owner
        except AttributeError:
            return self