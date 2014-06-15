def skip(attribute):
    """Make attribute to be skipped.
    
    Usage example::
    
      class Module(Module):
    
          @skip
          def method(self):
              pass
              
    In this case method will not be converted to run's attribute and
    will stay as regular python method.
    """
    setattr(attribute, '__isskippedattribute__', True)
    return attribute