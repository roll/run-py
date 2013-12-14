import types
import inspect
import importlib
from abc import ABCMeta
from .attribute import AttributeMixin

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

#     def __getitem__(self, key):
#         try:
#             return getattr(self, '_NamespaceMixin__'+key)
#         except AttributeError:
#             raise KeyError(key)
        
    @property
    def attributes(self):
        attributes = {}
        for cls in self.__class__.mro():
            for name, attr in cls.__dict__.items():
                if isinstance(attr, AttributeMixin):
                    attributes[name] = attr
        return attributes

        
def _import(module_name, attr_name):
    package_name = inspect.getmodule(NamespaceMixin).__package__
    module = importlib.import_module('.'+module_name, package_name)
    attr = getattr(module, attr_name)
    return attr                 