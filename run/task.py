import inspect
from .field import DependentField

class Task(DependentField):
    
    #Public
        
    def __call__(self, *args, **kwargs):
        self.resolve()
        return self.complete(*args, **kwargs)
    
    def complete(self, *args, **kwargs):
        pass
    

class MethodTask(Task):

    def __init__(self, method, **kwargs):
        super().__init__(**kwargs)
        self._method = method
        
    @property
    def __doc__(self):
        return self._method.__doc__

    def complete(self, *args, **kwargs):
        return self._method(self['module'], *args, **kwargs)
    
    def help(self):
        name = self._method.__name__
        signature = inspect.signature(self._method)
        docstring = inspect.getdoc(self._method)                    
        lines = []
        lines.append(name+str(signature))
        if docstring:
            lines.append(str(docstring))
        print('\n'.join(lines))      