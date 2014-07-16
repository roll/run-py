from box import jinja2
from .function import FunctionTask

class RenderTask(FunctionTask):

    # Public

    def __init__(self, *args, mode='file', **kwargs):
        try:
            function = getattr(jinja2, 'render_' + mode)
        except AttributeError:
            raise ValueError('Unsupported mode "{mode}".'.
                             format(mode=mode))
        kwargs.setdefault('context', self.meta_module)
        super().__init__(function, *args, **kwargs)
