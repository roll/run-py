from abc import ABCMeta, abstractmethod

class Unit(metaclass=ABCMeta):

    #Public

    @property
    @abstractmethod
    def unitname(self):
        pass
    
    @property
    @abstractmethod
    def unithelp(self):
        pass