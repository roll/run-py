import sys
from lib31.program import Program
from lib31.python import cachedproperty
from .command import Command
from .loader import ModuleLoader

class Program(Program):
    
    #Public
     
    #TODO: refactor   
    def __call__(self):
        if (self._command.help and 
            not self._command.attribute):
            print(self._command.program_help)
        else:
            #TODO: add error handling
            #TODO: fix not printing empty attributes
            for module in self._modules:
                result = module(
                    self._command.attribute,
                    *self._command.args, 
                    **self._command.kwargs)
                if result:
                    print(result)
         
    #Protected
    
    @cachedproperty
    def _command(self):
        return Command(self.argv)
    
    @cachedproperty
    def _modules(self):
        modules = []
        for module_class in self._module_classes:
            module = module_class(module=None)
            modules.append(module)
        return modules      
        
    @cachedproperty   
    def _module_classes(self):
        return self._module_loader.load(
            self._command.path, self._command.file)
        
    @cachedproperty   
    def _module_loader(self):
        return ModuleLoader()
    
    
program = Program(sys.argv)