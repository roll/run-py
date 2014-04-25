import os
import math
from run import Module, AutoModule, FindModule

class MainModule(Module):
    
    #Modules
    
    auto = AutoModule(
        sources=[math],
    )
    
    find = FindModule(
        filename='tasks.py',
        basedir=os.path.dirname(__file__),
    )