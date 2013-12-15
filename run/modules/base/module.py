from ...module import Module
from .input import InputVar
from .parse import ParseVar
from .render import RenderTask

class BaseModule(Module):

    #Public

    InputVar = InputVar
    ParseVar = ParseVar
    RenderTask = RenderTask