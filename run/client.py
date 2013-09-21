from abc import ABCMeta, abstractmethod

class Client(metaclass=ABCMeta):
    
    #Public
       
    @abstractmethod
    def request(self, request):
        pass #pragma: no cover
    
    
class SubprocessClient(Client):
    
    #Public
    
    pass  