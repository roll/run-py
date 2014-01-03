import os
import sys
from jinja2 import Environment, FileSystemLoader, Template
from jinja2.utils import concat
from run import Task

class RenderTask(Task):
    
    #Public
    
    #TODO: adjust to new basedir!
    def __init__(self, source, target, **kwargs):
        self._init_source = source
        self._init_target = target
        
    def complete(self):
        dirname, filename = os.path.split(os.path.abspath(self._source))
        environment = Environment(loader=FileSystemLoader(dirname))
        environment.template_class = NamespaceTemplate
        template = environment.get_template(filename)
        text = template.render(NamespaceContext(self.meta_module))
        with open(self._target, 'w') as file:
            file.write(text)
            

class NamespaceTemplate(Template):
    
    #Public
    
    def render(self, module_context):
        try:
            context = self.new_context(module_context, shared=True)
            return concat(self.root_render_func(context))
        except Exception:
            exc_info = sys.exc_info()
        return self.environment.handle_exception(exc_info, True)
        
        
class NamespaceContext:
    
    #Public
    
    def __init__(self, module):
        self._module = module
        
    def __contains__(self, key):
        return key in self._module.meta_attributes 
        
    def __getitem__(self, key):
        try:
            return getattr(self._module, key)
        except AttributeError:
            raise KeyError(key)        