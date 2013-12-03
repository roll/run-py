import os
import re
import sys
import inspect
import importlib
from subprocess import Popen, PIPE
from abc import ABCMeta, abstractmethod
from packgram.python import cachedproperty
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
    
    @cachedproperty
    def _decoder(self):
        return Decoder()
    
    @cachedproperty
    def _encoder(self):
        return Encoder()
    
    
class InprocessClient(Client):
    
    #Public
    
    def __init__(self, server_path):
        self._server_path = server_path
        
    def request(self, request, protocol=settings.default_protocol):
        try:
            method = getattr(self._run, request.method)
            result = method(*request.args, **request.kwargs)
            response = Response(result)
        except Exception as exception:
            response = Response(None, str(exception))
        return response
    
    #Protected
      
    @cachedproperty   
    def _run(self):
        dirname, filename = os.path.split(os.path.abspath(self._server_path))
        self._switch_to_server_directory(dirname)
        modulename = re.sub('\.pyc?', '', filename)
        #TODO: add no module handling
        module = importlib.import_module(modulename)
        for name in dir(module):
            attr = getattr(module, name)
            if (isinstance(attr, type) and
                not inspect.isabstract(attr) and
                issubclass(attr, Run)):
                return attr()
        else:
            raise RuntimeError('Run is not finded')
        
    def _switch_to_server_directory(self, dirname):
        os.chdir(dirname)
        sys.path.insert(0, dirname)      