import os
import render
from ...task import FunctionTask


class RenderTask(FunctionTask):

    # Public

    def __init__(self, *args, mode, **kwargs):
        try:
            function = getattr(render, 'render_' + mode)
        except AttributeError:
            raise ValueError(
                'Unsupported mode "{mode}".'.format(mode=mode))
        kwargs.setdefault('context', self.meta_module)
        super().__init__(function, *args, **kwargs)

    # TODO: rename target to savepath?
    # TODO: use pipe system instead of target?
    def meta_invoke(self, *args, target=None, **kwargs):
        result = super().meta_invoke(*args, **kwargs)
        if target is None:
            return result
        dirname = os.path.dirname(target)
        if dirname:
            os.makedirs(dirname, exist_ok=True)
        with open(target, 'w') as file:
            file.write(result)
