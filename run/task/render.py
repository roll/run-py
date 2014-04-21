from box.jinja2 import render_file 
from .function import FunctionTask

class RenderTask(FunctionTask):

    #Public
    
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('context', self.meta_module)
        super().__init__(render_file, *args, **kwargs)