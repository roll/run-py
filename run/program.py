import sys
from box.functools import cachedproperty
from box.logging import Program
from .command import Command
from .runtime import Run
from .settings import settings

class Program(Program):
         
    #Protected
    
    _command_class = Command    
    _settings = settings
    _run_class = Run    
    
    def _execute(self):
        self._run.run(
            self._command.attribute,
            *self._command.args, 
            **self._command.kwargs)
            
    @cachedproperty   
    def _run(self):
        return self._run_class(
            names=self._command.names,
            tags=self._command.tags,
            file=self._command.file,            
            basedir=self._command.basedir, 
            recursively=self._command.recursively,
            existent=self._command.existent,
            plain=self._command.plain)
    
        
program = Program(sys.argv)