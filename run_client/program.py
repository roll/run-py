import sys
from lib31.console import Command
from .responder import Responder
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
    def _responder(self):
        if not hasattr(self, '_responder_cached'):
            self._responder_cached = Responder(self._command.file)
        return self._responder_cached
    
    @property
    def _command(self):
        return Command(self._argv, schema=settings.command_schema)
    
           
program = Program(sys.argv)           