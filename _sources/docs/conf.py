import run
from box.sphinx import Settings

class Settings(Settings):
    
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
    
    html_theme = 'nature'
    

locals().update(Settings())