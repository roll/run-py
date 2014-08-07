from box import io
from .function import FunctionTask


class InputTask(FunctionTask):

    # Public

    def __init__(self, *args, **kwargs):
        function = io.enhanced_input
        super().__init__(function, *args, **kwargs)
