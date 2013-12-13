import os
from abc import ABCMeta, abstractmethod
from jinja2 import Environment, FileSystemLoader
from .property import Property

class Task(Property, metaclass=ABCMeta):
    
    #Public

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

    def complete(self, *args, **kwargs):
        return self._method(self._run, *args, **kwargs)
    
    #TODO: implement
    def help(self):
        if inspect.ismethod(attr):
            signature = inspect.signature(attr)
            docstring = inspect.getdoc(attr)                    
            lines = []
            lines.append(task_name+str(signature))
            if docstring:
                lines.append(str(docstring))
            print('\n'.join(lines))


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