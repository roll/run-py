import inspect
from abc import ABCMeta

class RunMeta(type):
    
    #Public
    
    pass


class Run(metaclass=RunMeta):
    
    #Public
    
    def list(self):
        "Print list of methods"
        methods = []
        for method in dir(self):
            if not method.startswith('_'):
                attr = getattr(self, method)
                if inspect.ismethod(attr):
                    methods.append(method)
        print('\n'.join(methods))
    
    def help(self, method):
        "Print method's help"        
        if not method.startswith('_'):
            attr = getattr(self, method)
            if inspect.ismethod(attr):
                signature = inspect.signature(attr)
                docstring = inspect.getdoc(attr)                    
                lines = []
                lines.append(method+str(signature))
                if docstring:
                    lines.append(str(docstring))
                print('\n'.join(lines))             