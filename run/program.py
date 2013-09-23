import sys
from lib31.console import Program
from .command import Command
from .client import SubprocessClient
from .request import Request

class Program(Program):
    
    #Public
        
    def __call__(self):
        client = SubprocessClient(self._command.server)
        request = Request(self._command.method, 
                          self._command.arguments, 
                          self._command.options)
        response = client.request(request)
        #TODO: improve
        print(response.result)
            
    #Protected
    
    #TODO: use cachedproperty
    @property
    def _command(self):
        return Command(self._argv)

    
program = Program(sys.argv)