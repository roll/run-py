from ...module import Module
from .input import InputVar, HiddenInputVar
from .parse import ParseVar
from .render import RenderTask

class BaseModule(Module):

    #Input

    InputVar = InputVar
    HiddenInputVar = HiddenInputVar
    
    #Parse
    
    ParseVar = ParseVar
    
    #Render
    
    RenderTask = RenderTask