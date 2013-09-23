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
        #TODO: add error handling
        response = client.request(request)
        #TODO: improve?
        if not response.error:
            print(response.result)
        else:
            print('Error: '+response.error)
            
    #Protected
    
    #TODO: use cachedproperty
    @property
    def _command(self):
        return Command(self.argv)

    
program = Program(sys.argv)