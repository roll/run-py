import sys
from lib31.program import Program
from lib31.python import cachedproperty
from .command import Command
from .module import ModuleLoader
from .task import Task

#TODO: add error handling
class Program(Program):
    
    #Public
     
    def __call__(self):
        for attribute in self._attributes:
            if isinstance(attribute, Task):
                result = attribute(
                    *self._command.args, 
                    **self._command.kwargs)
                if result:
                    print(result)
            else:
                print(attribute)           
         
    #Protected
    
    @cachedproperty
    def _attributes(self):
        attributes = []
        for module in self._modules:
            try:
                attribute = getattr(module, self._command.attribute)
                attributes.append(attribute)
            except AttributeError:
                if not self._command.existent:
                    raise
        return attributes
    
    @cachedproperty
    def _modules(self):
        modules = []
        for module_class in self._module_classes:
            module = module_class(module=None)
            modules.append(module)
        return modules
        
    @cachedproperty   
    def _module_classes(self):
        return list(self._module_loader.load(
            self._command.path, 
            self._command.file,
            self._command.recursively))
        
    @cachedproperty   
    def _module_loader(self):
        return ModuleLoader(
            names=self._command.names,
            tags=self._command.tags)
    
    @cachedproperty
    def _command(self):
        return Command(self.argv)
    
        
program = Program(sys.argv)