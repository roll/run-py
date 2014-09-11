from prompt import prompt
from ..task import FunctionTask
from ..var import Var


class PromptTask(FunctionTask):

    # Public

    def __init__(self, *args, **kwargs):
        super().__init__(prompt, *args, **kwargs)


class PromptVar(Var, PromptTask): pass
