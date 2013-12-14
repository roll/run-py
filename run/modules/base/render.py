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
        #TODO: fix run-module
        text = template.render(NamespaceDict(self.namespace))
        with open(self._target, 'w') as file:
            file.write(text)
            

class NamespaceDict(dict):
    
    def __init__(self, namespace):
        self._namespace = namespace
        
    def __getitem__(self, key):
        try:
            return getattr(self._namespace, key)
        except AttributeError:
            raise KeyError(key)        