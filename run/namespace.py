import types
import inspect
import importlib
from abc import ABCMeta
from .attribute import AttributeMixin

#Public

class NamespaceMeta(ABCMeta):
   
    #Public
   
    def __new__(cls, name, bases, attrs):
        for name, value in attrs.items():
            if not name.startswith('_'):
                #TODO: add other wrappings
                if isinstance(value, types.FunctionType):
                    MethodTask = _import('task', 'MethodTask')
                    attrs[name] = MethodTask(value)
        return super().__new__(cls, name, bases, attrs)


class NamespaceMixin(metaclass=NamespaceMeta):
    
    #Public

    def __getitem__(self, key):
        try:
            return getattr(self, '_NamespaceMixin__'+key)
        except AttributeError:
            raise KeyError(key)
        
    #Private   
        
    @property
    def __attributes(self):
        attributes = {}
        for cls in self.__class__.mro():
            for name, attr in cls.__dict__.items():
                if isinstance(attr, AttributeMixin):
                    attributes[name] = attr
        return attributes
    
    @property
    def __modules(self):
        Module = _import('module', 'Module') 
        return [name for name, prop 
                in self.__attributes.items() 
                if isinstance(prop, Module)]
    @property
    def __tasks(self):
        Task = _import('task', 'Task')
        return [name for name, prop 
                in self.__attributes.items() 
                if isinstance(prop, Task)]
    @property
    def __vars(self):
        Var = _import('var', 'Var')
        return [name for name, prop 
                in self.__attributes.items() 
                if isinstance(prop, Var)]


#Protected
        
def _import(module_name, attr_name):
    package_name = inspect.getmodule(NamespaceMixin).__package__
    module = importlib.import_module('.'+module_name, package_name)
    attr = getattr(module, attr_name)
    return attr                 