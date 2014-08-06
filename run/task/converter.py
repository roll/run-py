import inspect
from ..converter import Converter
from .method import MethodTask
from .prototype import TaskPrototype
from .task import Task

class task(Converter):
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

    def check_converted(self, obj):
        if isinstance(obj, self._TaskPrototype):
            return True
        if isinstance(obj, self._Task):
            return True
        return False

    def check_matched(self, obj):
        if inspect.isfunction(obj):
            return True
        return False

    def make(self, obj):
        prototype = MethodTask(obj, **self._kwargs)
        return prototype

    # Protected

    _Task = Task
    _TaskPrototype = TaskPrototype
