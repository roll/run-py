from abc import ABCMeta, abstractmethod

class Unpacker(metaclass=ABCMeta):
    
    #Public
    
    @abstractmethod
    def unpack(self):
        pass #pragma: no cover
    
    
class JSONUnpacker(Unpacker):
    
    #Public
    
    pass