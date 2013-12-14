from ...module import Module
from .parse import ParseVar
from .render import RenderTask

class BaseModule(Module):

    #Public

    RenderTask = RenderTask
    ParseVar = ParseVar