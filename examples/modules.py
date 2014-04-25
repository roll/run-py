from run import Module, AutoModule
from box import findtools

class MainModule(Module):
    
    #Modules
    
    auto = AutoModule(
        sources=[findtools],
    )