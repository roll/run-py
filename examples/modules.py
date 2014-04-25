import os
import math
from run import Module, AutoModule, FindModule, SubprocessModule

class MainModule(Module):
    
    #Modules
    
    auto = AutoModule(
        sources=[math],
    )
    
    find = FindModule(
        filename='tasks.py',
        basedir=os.path.dirname(__file__),
    )
    
    subprocess = SubprocessModule(
        mapping={
            'hello': 'echo "Hello World!"',
            'goodbye': 'echo "Goodbye World!"',
        },
    )