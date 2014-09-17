from .dependency import Dependency


class trigger(Dependency):
    """Decorate method to add trigger dependency.

    Examples
    --------
    Usage example::

      class Module(Module):

          @trigger('other_method')
          def method(self):
              pass

    Notes
    -----
    It's a shortcut for :class:`run.dependency.depend` decorator.
    """

    # Public

    def __init__(self, predecessor_name, *args,
                 on_success=True, on_fail=False, **kwargs):
        self.__on_success = on_success
        self.__on_fail = on_fail
        super().__init__(predecessor_name, *args, **kwargs)

    def resolve(self, failed=None):
        if failed is not None:
            if (self.__on_success and not failed or
                self.__on_fail and failed):
                self.invoke()
