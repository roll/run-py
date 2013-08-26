import sys
from lib31.console import Command
from .settings import settings

class Program:
    
    #Public
        
    def __init__(self, argv):
        self._argv = argv
        
    #TODO: implement
    def __call__(self):
        pass
            
    #Protected
    
    @property
    def _command(self):
        return Command(self._argv, schema=settings.command_schema)
    
           
program = Program(sys.argv)           