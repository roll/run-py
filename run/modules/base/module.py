from ...module import Module
from .parse import ParsedVar
from .render import RenderTask

class BaseModule(Module):

    #Public

    RenderTask = RenderTask
    ParsedVar = ParsedVar