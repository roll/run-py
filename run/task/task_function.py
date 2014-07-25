from box.functools import Decorator
from .method import MethodTask

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

    def __call__(self, method):
        prototype = self._task_class(method, **self._kwargs)
        return prototype

    def is_composite(self, *args, **kwargs):
        # Composite only if kwargs passed
        return not bool(args)

    # Protected

    _kwargs = {}
    _task_class = MethodTask
