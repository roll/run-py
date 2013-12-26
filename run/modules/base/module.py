from ...module import Module
from .input import InputVar, HiddenInputVar
from .load import LoadModule
from .parse import ParseVar
from .render import RenderTask

#TODO: add some DRY solution for module/__init__.py doubling
class BaseModule(Module):

    #Input

    InputVar = InputVar
    HiddenInputVar = HiddenInputVar
    
    #Load
    
    LoadModule = LoadModule
    
    #Parse
    
    ParseVar = ParseVar
    
    #Render
    
    RenderTask = RenderTask