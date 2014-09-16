import inspect
from ..converter import Converter
from .function import FunctionTask


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

    # override
    def _match(self, obj):
        if inspect.isfunction(obj):
            return True
        return False

    # override
    def _make(self, obj):
        prototype = FunctionTask(obj, bind=True, **self._kwargs)
        return prototype
