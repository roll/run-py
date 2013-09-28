import os
import sys
from lib31.console import Program
from lib31.python import cachedproperty
from .command import Command
from .client import SubprocessClient, InprocessClient
from .request import Request

class Program(Program):
    
    #Public
        
    def __call__(self):
        request = Request(self._command.method, 
                          self._command.args, 
                          self._command.kwargs)
        #TODO: add error handling
        response = self._client.request(request, self._command.protocol)
        #TODO: improve?
        if not response.error:
            if response.result:
                print(response.result)
        else:
            print('Error: '+response.error)
            
    #Protected
    
    @cachedproperty    
    def _client(self):
        if (os.path.isfile(self._command.server) and 
            os.access(self._command.server, os.X_OK)):
            return SubprocessClient(self._command.server)
        else:
            return InprocessClient(self._command.server)
    
    @cachedproperty
    def _command(self):
        return Command(self.argv)

    
program = Program(sys.argv)