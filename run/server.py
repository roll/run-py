import sys
from abc import ABCMeta, abstractmethod
from .decoder import Decoder
from .encoder import Encoder 

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
        text_request = self._argv[1]
        request = self._decoder.decode(text_request)
        response = self.respond(request)
        text_response = self._encoder.encode(response)
        sys.stdout.write(text_response)
        sys.stdout.flush()
    
    #Protected
    
    #TODO: use cachedproperty
    @property
    def _decoder(self):
        return Decoder()
    
    #TODO: use cachedproperty
    @property
    def _encoder(self):
        return Encoder()        