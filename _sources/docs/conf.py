import run
from box.sphinx import Settings

class Settings(Settings):
    
    #Build
        
    extensions = ['sphinx.ext.autodoc']
    master_doc = 'index'
    exclude_patterns = ['_build']
    pygments_style = 'sphinx'

    #Project
    
    project = 'run'
    author = 'roll'
    copyright = '2014, Respect31'
    version = run.version
    

locals().update(Settings())