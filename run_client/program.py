import sys
from lib31.console import Command
from .server import Server
from .settings import settings

class Program:
    
    #Public
        
    def __init__(self, argv):
        self._argv = argv
        
    #TODO: implement
    def __call__(self):
        pass
            
    #Protected
    
    #TODO: use cachedproperty
    @property
    def _server(self):
        if not hasattr(self, '_server_cached'):
            self._server_cached = Server(self._command.file)
        return self._server_cached
    
    @property
    def _command(self):
        return Command(self._argv, schema=settings.command_schema)
    
           
program = Program(sys.argv)           