from box.jinja2 import render_file 
from .task import Task

class RenderTask(Task):

    #Public

    def invoke(self, *args, **kwargs):
        kwargs.setdefault('context', self.meta_module)
        return render_file(*args, **kwargs)