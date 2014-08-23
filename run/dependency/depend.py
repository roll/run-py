from box.functools import Decorator


class depend(Decorator):
    """Decorate method to add custom dependency.

    Examples
    --------
    Dependency has to be instance of :class:`run.dependency.Dependency`::

      class Module(Module):

          @depend(require('other_method'))
          @depend(custom_dependency)
          def method(self):
              pass
    """

    # Public

    def __init__(self, dependency):
        self._dependency = dependency

    def __call__(self, method):
        return self._dependency(method)
