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
    autodoc_member_order = 'bysource'
    autodoc_default_flags = ['members', 'undoc-members', 'show-inheritance']    

    #Project
    
    project = 'run'
    author = 'roll'
    copyright = '2014, Respect31'
    version = run.version
    
    #HTML
    
    if not os.environ.get('READTHEDOCS', False):
        import sphinx_rtd_theme
        html_theme = 'sphinx_rtd_theme'
        html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
    

locals().update(Settings())