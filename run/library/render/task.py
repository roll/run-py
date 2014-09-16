import render
from ...task import FunctionTask


class RenderTask(FunctionTask):

    # Public

    def __init__(self, *args, mode, **kwargs):
        try:
            function = getattr(render, 'render_' + mode)
        except AttributeError:
            raise ValueError('Unsupported mode "{mode}".'.
                             format(mode=mode))
        kwargs.setdefault('context', self.meta_module)
        super().__init__(function, *args, **kwargs)
