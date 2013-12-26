import sys
from lib31.program import Program
from lib31.python import cachedproperty
from .command import Command
from .exception import RunException
from .module import ModuleLoader
from .task import Task

class Program(Program):
    
    #Public
     
    def __call__(self):
        try:
            self._execute()
        except Exception as exception:
            if self._command.debug:
                raise
            else:
                print('Error: '+str(exception))
         
    #Protected
    
    def _execute(self):
        for attribute in self._attributes:
            if isinstance(attribute, Task):
                result = attribute(
                    *self._command.args, 
                    **self._command.kwargs)
                if result:
                    print(result)
            else:
                print(attribute)  
    
    @cachedproperty
    def _attributes(self):
        attributes = []
        for module in self._modules:
            if hasattr(module, self._command.attribute):
                attribute = getattr(module, self._command.attribute)
                attributes.append(attribute)
            else:
                if not self._command.existent:
                    raise RunException('No attribute')
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