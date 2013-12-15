import os
import sys
from jinja2 import Environment, FileSystemLoader, Template
from jinja2.utils import concat
from ...task import Task

class RenderTask(Task):
    
    #Public
    
    def __init__(self, source, target, **kwargs):
        self._source = source
        self._target = target
        super().__init__(**kwargs)
        
    #Protected    
        
    def _complete(self):
        dirname, filename = os.path.split(os.path.abspath(self._source))
        environment = Environment(loader=FileSystemLoader(dirname))
        environment.template_class = NamespaceTemplate
        template = environment.get_template(filename)
        text = template.render(NamespaceContext(self._namespace))
        with open(self._target, 'w') as file:
            file.write(text)
            

class NamespaceTemplate(Template):
    
    #Public
    
    def render(self, namespace_context):
        try:
            context = self.new_context(namespace_context, shared=True)
            return concat(self.root_render_func(context))
        except Exception:
            exc_info = sys.exc_info()
        return self.environment.handle_exception(exc_info, True)
        
        
class NamespaceContext:
    
    #Public
    
    def __init__(self, namespace):
        self._namespace = namespace
        
    def __contains__(self, key):
        return key in self._namespace._attributes 
        
    def __getitem__(self, key):
        try:
            return getattr(self._namespace, key)
        except AttributeError:
            raise KeyError(key)        