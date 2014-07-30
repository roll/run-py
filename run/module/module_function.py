from ..task import task
from .module import Module

class module(task):
    """Decorate class to make module with default kwargs to invoke.

    There are two ways to use decorator:

    - Form without kwargs is designed for case when you have to convert class
      to module prototype immidiatly in class body to use some of it methods::

        class Module(Module):

            @module
            class module(Module):
                def default(self): pass

            module.meta_require('other_method')

    - Form with kwargs makes the same and adds default kwargs to invoke::

        class Module(Module):

            @var(**kwargs)
            class module(Module):
                def default(self, **kwargs): pass
    """

    # Public

    def invoke(self, cls):
        if not self._issubclass(cls, Module):
            raise TypeError(
                'Given class {cls} is not a Module'.
                format(cls=cls))
        prototype = cls(**self._kwargs)
        return prototype

    # Protected

    _issubclass = issubclass
