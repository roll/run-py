from .dependency import Dependency


class trigger(Dependency):
    """Decorate method to add trigger dependency.

    Usage example::

      class Module(Module):

          @trigger('other_method')
          def method(self):
              pass

    It's a shortcut for :class:`run.dependency.depend` decorator.
    """

    # Public

    def __init__(self, task, *args, **kwargs):
        self._on_success = kwargs.pop('on_success', True)
        self._on_fail = kwargs.pop('on_fail', False)
        super().__init__(task, *args, **kwargs)

    def resolve(self, failed=None):
        if self.enabled:
            if failed is not None:
                if (self._on_success and not failed or
                    self._on_fail and failed):
                    self.invoke()
