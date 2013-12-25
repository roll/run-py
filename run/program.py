import sys
from lib31.program import Program
from lib31.python import cachedproperty
from .command import Command
from .loader import ModuleLoader

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
        modules = self._module_loader.load('.', self.command.file)
        try:
            return modules[0]
        except IndexError:
            raise RuntimeError('Run is not finded')
        
        
    @cachedproperty   
    def _module_loader(self):
        return ModuleLoader()
    
    
program = Program(sys.argv)