from abc import ABCMeta, abstractmethod

class Server(metaclass=ABCMeta):
    
    #Public
    
    @abstractmethod
    def serve(self):
        pass #pragma: no cover
    
    @abstractmethod
    def respond(self, request):
        pass #pragma: no cover
    
    
class SubprocessServer(Server):
    
    #Public
    
    pass  