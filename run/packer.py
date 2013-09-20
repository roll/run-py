from abc import ABCMeta, abstractmethod

class Packer(metaclass=ABCMeta):
    
    #Public
    
    @abstractmethod
    def pack(self):
        pass #pragma: no cover
    
    
class JSONPacker(Packer):
    
    #Public
    
    pass