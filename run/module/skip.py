from box.functools import Decorator

class skip(Decorator):
    """Make task to be skipped.

    Usage example::

      class Module(Module):

          @skip
          def method(self):
              pass

    In this case method will not be converted to run's task and
    will stay as regular python method.
    """

    attribute_name = '_run_module_skip'

    def __call__(self, task):
        setattr(task, self.attribute_name, True)
        return task
