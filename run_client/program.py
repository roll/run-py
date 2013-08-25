import sys
from ..exceptions.exit import BaseExit
from .command import Command

class Program(object):
    
    def __init__(self, argv):
        self._command = Command(argv)
    
    def process(self):
        try:
            self._command.driver.process()
        except BaseExit as e:
            exit = ProgramExit(self._command, e)
            exit.process()       

    
class ProgramExit(object):
    
    def __init__(self, command, exception):
        self._command = command
        self._exception = exception

    def process(self):
        self._stream.write(self._text)
        sys.exit(self._exception.status)
        
    @property
    def _stream(self):
        if self._exception.status == 0:
            return sys.stdout
        else:
            return sys.stderr
        
    @property
    def _text(self):
        lines = []
        if self._exception.message:
            lines.append(self._exception.message)
        if self._exception.usage:
            lines.append(self._command.usage)
        if self._exception.help:
            lines.append(self._command.help)
        return '\n'.join(lines)+'\n'