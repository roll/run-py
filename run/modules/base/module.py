from ...module import Module
from .input import InputVar, HiddenInputVar
from .parse import ParseVar
from .render import RenderTask

#TODO: add some DRY solution for module/__init__.py doubling
class BaseModule(Module):

    #Input

    InputVar = InputVar
    HiddenInputVar = HiddenInputVar
    
    #Parse
    
    ParseVar = ParseVar
    
    #Render
    
    RenderTask = RenderTask