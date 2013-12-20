from functools import wraps
from .attribute import AttributeBuilder 
from .task import MethodTask

def require(tasks):
    @wraps
    def wrapper(method):
        if not isinstance(method, AttributeBuilder):
            builder = MethodTask(method)
        else:
            builder = method
        builder.require(tasks)
        return builder
    return wrapper

def trigger(tasks):
    @wraps
    def wrapper(method):
        if not isinstance(method, AttributeBuilder):
            builder = MethodTask(method)
        else:
            builder = method
        builder.trigger(tasks)
        return builder
    return wrapper    