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
    
    pass
    
#     def __new__(cls):
#         return super().__new__(cls, cls._build_string(substrings))   


class UnitHelp(str):
    
    #Public
    
    pass    