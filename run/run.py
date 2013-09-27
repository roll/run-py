import inspect
from abc import ABCMeta

class Run(metaclass=ABCMeta):
    
    #Public
    
    def list(self):
        """
        Prints list of methods
        """
        methods = []
        for method in dir(self):
            if not method.startswith('_'):
                attr = getattr(self, method)
                if inspect.ismethod(attr):
                    methods.append(method)
        return '\n'.join(methods)
    
    def help(self, method):
        """
        Prints method's help
        """        
        if not method.startswith('_'):
            attr = getattr(self, method)
            if inspect.ismethod(attr):
                signature = inspect.signature(attr)
                docstring = inspect.getdoc(attr)                    
                lines = []
                lines.append(method+str(signature))
                if docstring:
                    lines.append(str(docstring))
                return '\n'.join(lines)
        return ''