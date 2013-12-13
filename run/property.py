from abc import ABCMeta, abstractmethod

class Property(metaclass=ABCMeta):
    
    #Public
    
    def __init__(self, *args, **kwargs):
        self._require = kwargs.get('require', [])

    @abstractmethod
    def help(self):
        pass