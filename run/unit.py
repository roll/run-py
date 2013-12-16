from abc import ABCMeta, abstractmethod

class Unit(metaclass=ABCMeta):

    #Public

    @property
    @abstractmethod
    def unit_name(self):
        pass
    
    @property
    @abstractmethod
    def unit_help(self):
        pass
    
    
class UnitName(str):
    
    #Public
    
    def __new__(cls, namespace, attribute):
        qualname = '.'.join(namespace, attribute)
        return super().__new__(cls, qualname)
    
    def __init__(self, namespace, attribute):
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
    
    pass    