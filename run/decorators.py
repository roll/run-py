from functools import wraps
from .attribute import AttributeBuilder 
from .task import MethodTask

def require(tasks, *args, **kwargs):
    @wraps
    def wrapper(method):
        if not isinstance(method, AttributeBuilder):
            builder = MethodTask(method)
        else:
            builder = method
        builder.require(tasks, *args, **kwargs)
        return builder
    return wrapper

def trigger(tasks, *args, **kwargs):
    @wraps
    def wrapper(method):
        if not isinstance(method, AttributeBuilder):
            builder = MethodTask(method)
        else:
            builder = method
        builder.trigger(tasks, *args, **kwargs)
        return builder
    return wrapper    