from .method import MethodTask

class task:
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

    def __new__(cls, *args, **kwargs):
        if args:
            return cls._make_task(args[0], **kwargs)
        else:
            return super().__new__(cls)

    def __init__(self, **kwargs):
        self._kwargs = kwargs

    def __call__(self, method):
        return self._make_task(method, **self._kwargs)

    # Protected

    _task_class = MethodTask

    @classmethod
    def _make_task(cls, method, **kwargs):
        return cls._task_class(method, **kwargs)
