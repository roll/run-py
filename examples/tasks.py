import os 
from run import (Module, DerivedTask, DescriptorTask, FindTask, 
                 FunctionTask, InputTask, MethodTask, NullTask,
                 RenderTask, SubprocessTask, ValueTask)

class MainModule(Module):
    
    #Tasks
    
    derived = DerivedTask(
        task='method',
    )
    
    descriptor = DescriptorTask(
        descriptor=property(lambda self: True),
        meta_docstring='Return True.',                            
    )
        
    find = FindTask(
        string='find',
        getfirst=True,   
    )
    
    function = FunctionTask(
        function=os.path.abspath,
    )
    
    input = InputTask(
        prompt='Type here',                  
    )
    
    method = MethodTask(
        method=lambda self: 'Hello world!',
        meta_docstring='Return "Hello world!".',
    )
        
    null = NullTask(
        require=['subprocess'],                
    )
    
    render = RenderTask(
        source=os.path.abspath((__file__)),
    )
    
    subprocess = SubprocessTask(
        prefix='echo "Hello World!"',
    )
    
    value = ValueTask(
        value='value',
    )