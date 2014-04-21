import os 
from run import (Module, DerivedTask, DescriptorTask, FindTask, 
                 FunctionTask, InputTask, MethodTask)

class MainModule(Module):
    
    #Tasks
    
    derived = DerivedTask(
        task='method_task',
    )
    
    @DescriptorTask
    @property
    def descriptor(self):
        """Return True.
        """
        return True
        
    find = FindTask(
        string='test',
    )
    
    function = FunctionTask(
        function=os.path.abspath,
    )
    
    input = InputTask(
        prompt='Type here',                  
    )
        
    @MethodTask        
    def method(self):
        """Print "Hello world!".
        """
        print('Hello world!')    