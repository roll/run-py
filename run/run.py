import inspect

class Run:
    
    #Public
    
    def help(self, method=None):
        if not method:
            methods = []
            for method in dir(self):
                if not method.startswith('_'):
                    attr = getattr(self, method)
                    if inspect.ismethod(attr):
                        methods.append(method)
            return '\n'.join(methods)
        else:
            if not method.startswith('_'):
                attr = getattr(self, method)
                if inspect.ismethod(attr):
                    signature = str(inspect.signature(attr))
                    docstring = inspect.getdoc(attr)
                    return method+signature+'\n'+docstring