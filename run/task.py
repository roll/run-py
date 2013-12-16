import inspect
from .attribute import AssociatedAttribute
from .unit import UnitHelp

class Task(AssociatedAttribute):
    
    #Public
        
    def __call__(self, *args, **kwargs):
        self.resolve()
        return self.complete(*args, **kwargs)
    
    def complete(self, *args, **kwargs):
        pass


class MethodTask(Task):
    
    #Public

    def __init__(self, method, **kwargs):
        super().__init__(**kwargs)
        self._method = method
        
    @property
    def __doc__(self):
        return self._method.__doc__
    
    def complete(self, *args, **kwargs):
        return self._method(self.namespace, *args, **kwargs)
    
    def unit_help(self):
        return UnitHelp(inspect.signature(self._method),
                        inspect.getdoc(self._method))
