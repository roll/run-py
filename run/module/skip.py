from box.functools import Decorator

class skip(Decorator):
    """Make attribute to be skipped.

    Usage example::

      class Module(Module):

          @skip
          def method(self):
              pass

    In this case method will not be converted to run's attribute and
    will stay as regular python method.
    """

    attribute_name = '_run_module_skip'

    def __call__(self, attribute):
        setattr(attribute, self.attribute_name, True)
        return attribute
