import types
from abc import ABCMeta
from functools import wraps
from .task import MethodTask

class ModuleMeta(ABCMeta):
   
    def __new__(cls, name, bases, attrs):
        for name, value in attrs.items():
            if isinstance(value, types.FunctionType):
                attrs[name] = MethodTask(value)
        return super().__new__(cls, name, bases, attrs)


class Module(metaclass=ModuleMeta):

    #Public

    pass


def require(*task_names):
    @wraps
    def wrapper(method):
        return MethodTask(method, require=task_names)
    return wrapper