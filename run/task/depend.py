from ..helpers import Function


class depend(Function):
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

    protocol = Function.DECORATOR

    def __init__(self, dependency):
        self.__dependency = dependency

    def __call__(self, method):
        return self.__dependency(method)
