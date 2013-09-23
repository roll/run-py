import inspect

class Run:
    
    #Public
    
    def help(self, method=None):
        if not method:
            methods = []
            for name in dir(self):
                attr = getattr(self, name)
                if  not name.startswith('_') and inspect.ismethod(attr):
                    methods.append(name)
            return '\n'.join(methods)
        else:
            pass
            #TODO: implement                    