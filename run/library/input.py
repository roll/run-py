from box import io
from ..task import FunctionTask
from ..var import Var


class InputTask(FunctionTask):

    # Public

    def __init__(self, *args, **kwargs):
        function = io.enhanced_input
        super().__init__(function, *args, **kwargs)


class InputVar(Var, InputTask): pass
