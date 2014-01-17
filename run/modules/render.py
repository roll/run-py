from box.jinja2 import render_file
from run import Module     
        
class RenderModule(Module):
    
    #Public

    def render_file(self, *args, **kwargs):
        return render_file(*args, **kwargs)