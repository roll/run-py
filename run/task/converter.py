import inspect
from ..converter import Converter
from .method import MethodTask


class task(Converter):
    """Decorate method to make task with default kwargs to invoke.

    Examples
    --------
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

    # Protected

    def _match(self, obj):
        if inspect.isfunction(obj):
            return True
        return False

    def _make(self, obj):
        prototype = MethodTask(obj, **self._kwargs)
        return prototype
