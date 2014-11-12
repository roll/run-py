from .dependency import Dependency


class require(Dependency):
    """Decorate method to add require dependency.

    Examples
    --------
    Usage example::

      class Module(Module):

          @require('other_method')
          def method(self):
              pass

    Notes
    -----
    It's a shortcut for :class:`run.dependency.depend` decorator.
    """

    # Public

    def __init__(self, __target, *args, **kwargs):
        self.__is_resolved = False
        super().__init__(__target, *args, **kwargs)

    def resolve(self, fail=None):
        if fail is None:
            if not self.__is_resolved:
                self.invoke()
                self.__is_resolved = True
