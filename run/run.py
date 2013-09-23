import inspect

class Run:
    
    #Public
    
    #TODO: refactor
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
                    signature = inspect.signature(attr)
                    docstring = inspect.getdoc(attr)                    
                    lines = []
                    lines.append(method+str(signature))
                    if docstring:
                        lines.append(str(docstring))
                    return '\n'.join(lines)
        return ''