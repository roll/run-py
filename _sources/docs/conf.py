import os
import run
from box.sphinx import Settings

class Settings(Settings):
    
    #Documentation:
    #http://sphinx-doc.org/config.html

    #Build
        
    extensions = ['sphinx.ext.autodoc']
    master_doc = 'index'
    pygments_style = 'sphinx'

    #Project
    
    project = 'run'
    author = 'roll'
    copyright = '2014, Respect31'
    version = run.version
    
    #HTML
    
    @property
    def html_theme(self):
        if os.environ.get('READTHEDOCS', None):
            return 'default'
        else:
            return 'nature'
    

locals().update(Settings())