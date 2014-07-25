from ..task import task
from .descriptor import DescriptorVar

class var(task):
    """Decorate method to make var with default kwargs to invoke.

    There are two ways to use decorator:

    - Form without kwargs is designed for case when you have to convert method
      to var prototype immidiatly in class body to use some of it methods::

        class Module(Module):

            @var
            def method(self):
                pass

            method.require('other_method')

    - Form with kwargs makes the same and adds default kwargs to invoke::

        class Module(Module):

            @var(**kwargs)
            def method(self, **kwargs):
                pass
    """

    # Public

    def __call__(self, method):
        prototype = self._task_class(property(method), **self._kwargs)
        return prototype

    # Protected

    _task_class = DescriptorVar
