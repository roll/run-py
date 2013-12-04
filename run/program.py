import os
import re
import sys
import inspect
import importlib
from packgram.python import cachedproperty
from packgram.console import Program
from .command import Command
from .request import Request
from .run import Run

class Program(Program):
    
    #Public
        
    def __call__(self):
        request = Request(self._command.method, 
                          self._command.args, 
                          self._command.kwargs)
        #TODO: add error handling
        response = self._client.request(request, self._command.protocol)
        #TODO: improve?
        if not response.error:
            if response.result:
                print(response.result)
        else:
            print('Error: '+response.error)
            
    #Protected
    
    @cachedproperty
    def _command(self):
        return Command(self.argv)
    
    @cachedproperty   
    def _run(self):
        dirname, filename = os.path.split(os.path.abspath(self._server_path))
        self._switch_to_server_directory(dirname)
        modulename = re.sub('\.pyc?', '', filename)
        #TODO: add no module handling
        module = importlib.import_module(modulename)
        for name in dir(module):
            attr = getattr(module, name)
            if (isinstance(attr, type) and
                not inspect.isabstract(attr) and
                issubclass(attr, Run)):
                return attr()
        else:
            raise RuntimeError('Run is not finded')
        
    def _switch_to_server_directory(self, dirname):
        os.chdir(dirname)
        sys.path.insert(0, dirname) 
    
program = Program(sys.argv)