from functools import wraps
from .task import MethodTask

#TODO: fix logic method/MethodTask/MethodBuilder

def require(tasks):
    @wraps
    def wrapper(method):
        return MethodTask(method, require=tasks)
    return wrapper

def trigger(tasks):
    @wraps
    def wrapper(method):
        return MethodTask(method, trigger=tasks)
    return wrapper    