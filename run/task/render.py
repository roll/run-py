from box.jinja2 import render_file 
from .task import Task

class RenderTask(Task):

    #Public

    def __init__(self, source, target=None):
        self._source = source
        self._target = target
        
    def invoke(self):
        return render_file(self._source, 
                           context=self.meta_module, 
                           target=self._target)