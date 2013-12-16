import inspect

class Unit:

    #Public

    @property
    def unitname(self):
        return UnitName()
    
    @property
    def unithelp(self):
        return UnitHelp(docstring=inspect.getdoc(self))
    
    
class UnitName(str):
    
    #Public
    
    def __new__(cls, namespace='', attribute=''):
        name = '.'.join(filter(None, [namespace, attribute]))
        return super().__new__(cls, name)
    
    def __init__(self, namespace='', attribute=''):
        self._namespace = namespace
        self._attribute = attribute
    
    @property    
    def namespace(self):
        return self._namespace
    
    @property
    def attribute(self):
        return self._attribute    
    

class UnitHelp(str):
    
    #Public
    
    def __new__(cls, signature='', docstring=''):
        hlp = '\n'.join(filter(None, [signature, docstring]))
        return super().__new__(cls, hlp)
    
    def __init__(self, signature='', docstring=''):
        self._signature = signature
        self._docstring = docstring
    
    @property    
    def signature(self):
        return self._signature
    
    @property
    def docstring(self):
        return self._docstring      