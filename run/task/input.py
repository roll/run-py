from box import io
from .function import FunctionTask


class InputTask(FunctionTask):

    # Public

    def __init__(self, *args, **kwargs):
        super().__init__(io.enhanced_input, *args, **kwargs)
