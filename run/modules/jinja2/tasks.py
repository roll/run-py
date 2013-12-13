import os
from jinja2 import Environment, FileSystemLoader
from ...task import Task

class RenderTask(Task):
    
    def __init__(self, source, target, **kwargs):
        super().__init__(**kwargs)
        self._source = source
        self._target = target
        
    def complete(self):
        dirname, filename = os.path.split(os.path.abspath(self._source))
        environment = Environment(loader=FileSystemLoader(dirname))
        template = environment.get_template(filename)
        text = template.render(self._run)
        with open(self._target, 'w') as file:
            file.write(text)