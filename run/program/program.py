import sys
from box.functools import cachedproperty
from box.logging import Program
from ..machine import Machine
from ..settings import settings
from .command import Command

class Program(Program):
         
    #Protected
    
    _command_class = Command    
    _machine_class = Machine
    _settings = settings
    
    def _execute(self):
        self._machine.process(
            self._command.attribute,
            *self._command.args, 
            **self._command.kwargs)
            
    @cachedproperty   
    def _machine(self):
        machine = self._machine_class(
            names=self._command.names,
            tags=self._command.tags,
            file=self._command.file,            
            basedir=self._command.basedir, 
            recursively=self._command.recursively,
            existent=self._command.existent,
            plain=self._command.plain)
        return machine
    
        
program = Program(sys.argv)