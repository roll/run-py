from builtins import isinstance, issubclass
from ..task import task
from .module import Module


class module(task):
    """Decorate class to make module with default kwargs to invoke.

    Examples
    --------
    There are two ways to use decorator:

    - Form without kwargs is designed for case when you have to convert class
      to module prototype immidiatly in class body to use some of it methods::

        class Module(Module):

            @module
            class module(Module):
                def default(self): pass

            module.Require('other_method')

    - Form with kwargs makes the same and adds default kwargs to invoke::

        class Module(Module):

            @var(**kwargs)
            class module(Module):
                def default(self, **kwargs): pass
    """

    # Public

    def match(self, obj):
        if isinstance(obj, type):
            if issubclass(obj, Module):
                return True
        return False

    def make(self, obj):
        prototype = obj(*self.args, **self.kwargs)
        return prototype
