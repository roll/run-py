import os
import re
import sys
import inspect
import importlib
from lib31.program import Program
from lib31.python import cachedproperty
from .command import Command
from .loader import ModuleLoader
from .module import Module

class Program(Program):
    
    #Public
        
    def __call__(self):
        if (self.command.help and not self.command.attribute):
            print(self.command.program_help)
        else:
            #TODO: add error handling
            result = self._module(self.command.attribute,
                *self.command.args, **self.command.kwargs)
            #TODO: fix not printing empty attributes
            if result:
                print(result)
    
    @cachedproperty
    def command(self):
        return Command(self.argv)
         
    #Protected
    
    @cachedproperty   
    def _module(self):
        dirname, filename = os.path.split(os.path.abspath(self.command.file))
        self._switch_to_directory(dirname)
        modulename = re.sub('\.pyc?', '', filename)
        #TODO: add no module handling
        module = importlib.import_module(modulename)
        for name in dir(module):
            attr = getattr(module, name)
            if (isinstance(attr, type) and
                issubclass(attr, Module) and
                inspect.getmodule(attr) == module and
                not inspect.isabstract(attr)):
                return attr(module=None)
        else:
            raise RuntimeError('Run is not finded')
        
    def _switch_to_directory(self, dirname):
        os.chdir(dirname)
        sys.path.insert(0, dirname) 
    
    
program = Program(sys.argv)