import os
from abc import ABCMeta, abstractmethod
from jinja2 import Environment, FileSystemLoader

class Task(metaclass=ABCMeta):
    
    #Public

    @abstractmethod
    def complete(self, values):
        pass #pragma: no cover
  

class RenderTask(Task):
    
    def __init__(self, source, target):
        self._source = source
        self._target = target
        
    def complete(self, values):
        dirname, filename = os.path.split(os.path.abspath(self._source))
        environment = Environment(loader=FileSystemLoader(dirname))
        template = environment.get_template(filename)
        text = template.render(values)
        with open(self._target, 'w') as file:
            file.write(text)      