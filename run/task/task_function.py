from box.functools import Decorator
from .method import MethodTask
from .prototype import TaskPrototype
from .task import Task

class task(Decorator):
    """Decorate method to make task with default kwargs to invoke.

    There are two ways to use decorator:

    - Form without kwargs is designed for case when you have to convert method
      to task prototype immidiatly in class body to use some of it methods::

        class Module(Module):

            @task
            def method(self):
                pass

            method.require('other_method')

    - Form with kwargs makes the same and adds default kwargs to invoke::

        class Module(Module):

            @task(**kwargs)
            def method(self, **kwargs):
                pass
    """

    # Public

    def __init__(self, **kwargs):
        self._kwargs = kwargs

    def __call__(self, obj):
        result = obj
        if (not isinstance(obj, self._task_prototype_class) and
            not isinstance(obj, self._task_class)):
            result = self.invoke(obj)
        return result

    def invoke(self, method):
        prototype = MethodTask(method, **self._kwargs)
        return prototype

    # Overriding
    def is_composite(self, *args, **kwargs):
        # Composite only if kwargs passed
        return not bool(args)

    # Protected

    _kwargs = {}
    _task_class = Task
    _task_prototype_class = TaskPrototype
