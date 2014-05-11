from box import findtools 
from .function import FunctionTask

class FindTask(FunctionTask):

    #Public
    
    def __init__(self, *args, mode='strings', **kwargs):
        try:
            function = getattr(findtools, 'find_'+mode)
        except AttributeError:
            raise ValueError('Unsupported mode "{mode}".'.
                             format(mode=mode))
        super().__init__(function, *args, **kwargs)