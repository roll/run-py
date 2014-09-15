import find
from ...task import FunctionTask


class FindTask(FunctionTask):

    # Public

    def __init__(self, *args, mode='strings', **kwargs):
        try:
            function = getattr(find, 'find_' + mode)
        except AttributeError:
            raise ValueError('Unsupported mode "{mode}".'.
                             format(mode=mode))
        super().__init__(function, *args, **kwargs)
