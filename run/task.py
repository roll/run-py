import os
from abc import ABCMeta, abstractmethod
from jinja2 import Environment, FileSystemLoader

class Task(metaclass=ABCMeta):
    
    #Public
    
    def __init__(self, *args, **kwargs):
        self._require = kwargs.get('require', [])

    def __get__(self, run, runclass=None):
        self._run = run
        return self
        
    def __call__(self, *args, **kwargs):
        for task_name in self._require:
            task = getattr(self._run, task_name)
            task()
        self.complete(*args, **kwargs)

    @abstractmethod
    def complete(self, *args, **kwargs):
        pass #pragma: no cover


class MethodTask(Task):

    def __init__(self, method, **kwargs):
        super().__init__(**kwargs)
        self._method = method
        
    @property
    def __doc__(self):
        return self._method.__doc__

    @abstractmethod
    def complete(self, *args, **kwargs):
        return self._method(*args, **kwargs)


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