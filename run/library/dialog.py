from dialog import Dialog
from ..task import FunctionTask
from ..var import Var


# TODO: rebase from FunctionTask?
class DialogTask(FunctionTask):

    # Public

    def __init__(self, *args, **kwargs):
        self.__dialog = Dialog()
        function = self.__dialog.question
        if kwargs.get('message', False):
            function = self.__dialog.message
        super().__init__(function, *args, **kwargs)


class DialogVar(Var, DialogTask): pass
