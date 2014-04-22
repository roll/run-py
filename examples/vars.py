import os 
from run import (Module, DerivedVar, DescriptorVar, FindVar, 
                 FunctionVar, InputVar, MethodVar, NullVar,
                 RenderVar, SubprocessVar, ValueVar)

class MainModule(Module):
    
    #Vars
    
    derived = DerivedVar(
        task='method',
    )
    
    descriptor = DescriptorVar(
        descriptor=property(lambda self: True),
        meta_docstring='Return True.',                            
    )
        
    find = FindVar(
        string='test',
    )
    
    function = FunctionVar(
        function=os.path.abspath,
    )
    
    input = InputVar(
        prompt='Type here',                  
    )
    
    method = MethodVar(
        method=lambda self: 'Hello world!',
        meta_docstring='Return "Hello world!".',
    )
        
    null = NullVar(
        require=['method'],                
    )
    
    render = RenderVar(
        source='/etc/hosts',
    )
    
    subprocess = SubprocessVar(
        prefix='echo "Hello World!"',
    )
    
    value = ValueVar(
        value='value',
    )