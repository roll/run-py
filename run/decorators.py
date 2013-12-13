from functools import wraps
from .task import MethodTask

def require(tasks):
    @wraps
    def wrapper(method):
        return MethodTask(method, require=tasks)
    return wrapper