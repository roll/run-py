from dialog import Dialog
from ...task import FunctionTask


# TODO: rebase from FunctionTask?
class DialogTask(FunctionTask):

    # Public

    def __init__(self, *args, listen=False, **kwargs):
        self.__dialog = Dialog()
        if listen:
            function = self.__dialog.listen
        elif kwargs.get('message', False):
            function = self.__dialog.message
        elif kwargs.get('question', False):
            function = self.__dialog.question
        else:
            raise ValueError('Unsupported mode')
        super().__init__(function, *args, **kwargs)
