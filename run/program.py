import sys
from lib31.program import Program
from lib31.python import cachedproperty
from .command import Command
from .module import ModuleLoader

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
            self._command.path, self._command.file,
            recursively=self._command.recursively)
        
    @cachedproperty   
    def _module_loader(self):
        return ModuleLoader(names=self._command.names,
                            tags=self._command.tags)
    
    
program = Program(sys.argv)