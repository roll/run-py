import os
import re
from abc import ABCMeta, abstractmethod
from subprocess import Popen, PIPE
from lib31.python import import_module
from .decoder import Decoder
from .encoder import Encoder
from .response import Response
from .run import Run
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
    
    
class InprocessClient(Client):
    
    #Public
    
    def __init__(self, server_path):
        self._server_path = server_path
        
    def request(self, request):
        try:
            method = getattr(self._run, request.method)
            result = method(*request.arguments, **request.options)
            response = Response(result)
        except Exception as exception:
            response = Response(None, str(exception))
        return response
    
    #Protected
      
    #TODO: use cachedproperty
    @property   
    def _run(self):
        path, name = os.path.split(os.path.abspath(self._server_path))
        name = '.'+re.sub('\.pyc?', '', name)
        #TODO: add no module handling
        module = import_module(name, path)
        for name in dir(module):
            attr = getattr(module, name)
            if isinstance(attr, type) and issubclass(attr, Run):
                return attr()
        else:
            raise RuntimeError('Run is not finded')