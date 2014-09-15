import render
from ...frame.task import FunctionTask


# TODO: add mode use with find_files?
class RenderTask(FunctionTask):

    # Public

    def __init__(self, *args, mode='file', **kwargs):
        try:
            function = getattr(render, 'render_' + mode)
        except AttributeError:
            raise ValueError('Unsupported mode "{mode}".'.
                             format(mode=mode))
        kwargs.setdefault('context', self.meta_module)
        super().__init__(function, *args, **kwargs)
