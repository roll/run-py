import inspect
from .attribute import DependentAttributeMixin

class Task(DependentAttributeMixin):
    
    #Public
        
    def __call__(self, *args, **kwargs):
        self._resolve()
        return self._complete(*args, **kwargs)
    
    #Protected
    
    def _complete(self, *args, **kwargs):
        pass
    

class MethodTask(Task):
    
    #Public

    def __init__(self, method, **kwargs):
        super().__init__(**kwargs)
        self._method = method
        
    @property
    def __doc__(self):
        return self._method.__doc__
    
    def help(self):
        name = self._method.__name__
        signature = inspect.signature(self._method)
        docstring = inspect.getdoc(self._method)                    
        lines = []
        lines.append(name+str(signature))
        if docstring:
            lines.append(str(docstring))
        print('\n'.join(lines))

    #Protected

    def _complete(self, *args, **kwargs):
        return self._method(self._namespace, *args, **kwargs)          