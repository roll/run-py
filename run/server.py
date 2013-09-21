from abc import ABCMeta, abstractmethod

class Server(metaclass=ABCMeta):
    
    #Public
    
    def __init__(self, run):
        self._run = run
    
    @abstractmethod
    def serve(self):
        pass #pragma: no cover
    
    @abstractmethod
    def respond(self, request):
        pass #pragma: no cover
    
    
class SubprocessServer(Server, metaclass=ABCMeta):
    
    #Public
    
    def __init__(self, run, argv):
        super().__init__(run)
        self._argv = argv
        
    #TODO: implement
    def serve(self):
        pass