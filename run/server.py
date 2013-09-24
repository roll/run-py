import sys
from abc import ABCMeta, abstractmethod
from .decoder import Decoder
from .encoder import Encoder 
from .response import Response

class Server(metaclass=ABCMeta):
    
    #Public
    
    def __init__(self, run):
        self._run = run
    
    @abstractmethod
    def serve(self):
        pass #pragma: no cover
    
    def respond(self, request):
        try:
            method = getattr(self.run, request.method)
            result = method(*request.arguments, **request.options)
            response = Response(result)
        except Exception as exception:
            response = Response(None, str(exception))
        return response
    
    @property
    def run(self):
        return self._run
    
    
class SubprocessServer(Server):
    
    #Public
    
    def __init__(self, run, argv):
        super().__init__(run)
        self._argv = argv
        
    def serve(self):
        #TODO: add argv check
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