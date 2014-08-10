from .dependency import Dependency


class require(Dependency):
    """Decorate method to add require dependency.

    Usage example::

      class Module(Module):

          @require('other_method')
          def method(self):
              pass

    It's a shortcut for :class:`run.dependency.depend` decorator.
    """

    # Public

    def __init__(self, predecessor_name, *args, **kwargs):
        self._is_resolved = False
        super().__init__(predecessor_name, *args, **kwargs)

    def resolve(self, failed=None):
        if self.enabled:
            if failed is None:
                if not self._is_resolved:
                    self.invoke()
                    self._is_resolved = True
