import os
from abc import ABCMeta, abstractmethod
from subprocess import Popen, PIPE
from .decoder import Decoder
from .encoder import Encoder
from .settings import settings

class Client(metaclass=ABCMeta):
    
    #Public
       
    @abstractmethod
    def request(self, request, protocol):
        pass #pragma: no cover
    
    
class SubprocessClient(Client):
    
    #Public
    
    def __init__(self, server_path):
        self._server_path = server_path
    
    def request(self, request, protocol=settings.default_protocol):
        text_request = self._encoder.encode(request, protocol)
        arguments = [os.path.abspath(self._server_path), text_request]
        #TODO: add filtering, print no protocol output
        with Popen(arguments, stdout=PIPE) as subprocess:
            text_response = subprocess.stdout.read().decode()
        response = self._decoder.decode(text_response)
        return response
        
    #Protected
    
    #TODO: use cachedproperty
    @property
    def _decoder(self):
        return Decoder()
    
    #TODO: use cachedproperty
    @property
    def _encoder(self):
        return Encoder() 