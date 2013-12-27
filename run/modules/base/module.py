#TODO: remove __init__.py doubling
from run import Module
from .cluster import ClusterModule
from .composite import CompositeTask
from .input import InputVar, HiddenInputVar
from .load import LoadModule
from .parse import ParseVar
from .render import RenderTask

class BaseModule(Module):
    
    #Cluster
    
    ClusterModule = ClusterModule
    
    #Composite
    
    CompositeTask = CompositeTask

    #Input

    InputVar = InputVar
    HiddenInputVar = HiddenInputVar
    
    #Load
    
    LoadModule = LoadModule
    
    #Parse
    
    ParseVar = ParseVar
    
    #Render
    
    RenderTask = RenderTask