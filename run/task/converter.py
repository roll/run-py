import inspect
from sugarbowl import Function
from .error import ConvertError
from .method import MethodTask
from .prototype import Prototype
from .skip import skip
from .task import Task


class task(Function):
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

    # Public

    def __init__(self, *args, **kwargs):
        self.__args = args
        self.__kwargs = kwargs

    def __call__(self, obj):
        if self.__check_converted(obj):
            return obj
        if self.__check_eligible(obj):
            if self.match(obj):
                return self.make(obj)
        raise ConvertError(
            'Converter "{self}" is not suitable converter '
            'for the given object "{obj}" convertation.'.
            format(self=self, obj=obj))

    def protocol(self, *args, **kwargs):
        try:
            if (inspect.isfunction(args[0]) or
                isinstance(args[0], (Task, Prototype))):
                return Function.FUNCTION
        except IndexError:
            pass
        return Function.DECORATOR

    @property
    def args(self):
        return self.__args

    @property
    def kwargs(self):
        return self.__kwargs

    def match(self, obj):
        if inspect.isfunction(obj):
            return True
        return False

    def make(self, obj):
        prototype = MethodTask(obj, *self.args, **self.kwargs)
        return prototype

    # Private

    def __check_converted(self, obj):
        return isinstance(obj, (Task, Prototype))

    def __check_eligible(self, obj):
        if isinstance(obj, staticmethod):
            return False
        if isinstance(obj, classmethod):
            return False
        if getattr(obj, skip.attribute_name, False):
            return False
        if getattr(obj, '__isabstractmethod__', False):
            return False
        return True
