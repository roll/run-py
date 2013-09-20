from abc import ABCMeta, abstractmethod

class ContentPacker(metaclass=ABCMeta):
    
    #Public
    
    @abstractmethod
    def pack(self):
        pass #pragma: no cover
    
    
class JSONContentPacker(ContentPacker):
    
    #Public
    
    pass