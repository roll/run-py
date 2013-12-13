from lib31.python import cachedproperty

class Field:
    
    #Public
    
    def __init__(self, *args, **kwargs):
        self.__owner = self
        self.__params = kwargs
    
    def __get__(self, owner, owner_class=None):
        self.__owner = owner
        return self
    
    def help(self):
        pass
    
    #Protected

    @cachedproperty
    def _manager(self):
        from .manager import Manager
        return Manager(self, self.__owner, self.__params)    