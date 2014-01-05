import os
import sys
from lib31.python import cachedproperty
from jinja2 import Environment, FileSystemLoader, Template
from jinja2.utils import concat
from run import Task

class RenderTask(Task):
    
    #Public
    
    #TODO: adjust to new basedir!
    def __init__(self, source, target):
        self._source = source
        self._target = target
        
    def complete(self):
        text = self._template.render(self._context)
        with self._open_operator(self._target, 'w') as file:
            file.write(text)
            
    #Protected
    
    _environment_class = Environment
    _file_system_loader_class = FileSystemLoader
    _module_template_class = property(lambda self: ModuleTemplate)
    _module_context_class = property(lambda self: ModuleContext)
    _open_operator = staticmethod(open)
    
    @cachedproperty
    def _context(self):
        context = self._module_context_class(self.meta_module)
        return context  
    
    @cachedproperty
    def _template(self):
        dirname, filename = os.path.split(os.path.abspath(self._source))
        loader = self._file_system_loader_class(dirname)
        environment = self._environment_class(loader=loader)
        environment.template_class = self._module_template_class
        template = environment.get_template(filename)
        return template


class ModuleTemplate(Template):
    
    #Public
    
    def render(self, module_context):
        try:
            context = self.new_context(module_context, shared=True)
            return self._concat_operator(self.root_render_func(context))
        except Exception:
            exc_info = sys.exc_info()
            return self.environment.handle_exception(exc_info, True)
    
    #Protected
    
    _concat_operator = staticmethod(concat)
        
        
class ModuleContext:
    
    #Public
    
    def __init__(self, module):
        self._module = module
        
    #TODO: hasattr?? (it hits Var.retrieve)
    def __contains__(self, key):
        return hasattr(self._module, key) 
        
    def __getitem__(self, key):
        try:
            return getattr(self._module, key)
        except AttributeError:
            raise KeyError(key)        