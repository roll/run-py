from abc import ABCMeta, abstractmethod

class ContentUnpacker(metaclass=ABCMeta):
    
    #Public
    
    @abstractmethod
    def unpack(self):
        pass #pragma: no cover
    
    
class JSONContentUnpacker(ContentUnpacker):
    
    #Public
    
    pass