import sys
from lib31.console import Program
from .client import SubprocessClient
from .request import Request
from .settings import settings

class Program(Program):
    
    #Public
        
    def __call__(self):
        client = SubprocessClient(self._command.server)
        response = client.request(self._request)
        print(response.content)
            
    #Protected
        
    @property
    def _request(self):
        #TODO: reimplement
        method = self._command.method
        arguments, options = self._parse_parameters(self._command.parameters)
        request = Request(method, arguments, options)
        return request
    
    #TODO: implement
    def _parse_parameters(self):
        pass
        
    @property
    def _command_schema(self):
        return settings.command_schema

    
program = Program(sys.argv)