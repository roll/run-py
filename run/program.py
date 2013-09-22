import sys
from lib31.console import Program
from .client import SubprocessClient
from .request import Request
from .settings import settings

class Program(Program):
    
    #Public
        
    def __call__(self):
        client = SubprocessClient(self._command.server)
        #TODO: reimplement
        request = Request(self._command.protocol, self._command.content)
        response = client.request(request)
        print(response.content)
            
    #Protected
    
    @property
    def _command_schema(self):
        return settings.command_schema

    
program = Program(sys.argv)