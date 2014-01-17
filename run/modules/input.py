from box.input import input
from run import Module

class InputModule(Module):
    
    #Public

    def input(self, *args, **kwargs):
        return input(*args, **kwargs)