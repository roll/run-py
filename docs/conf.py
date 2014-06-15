import os
import run
from packgram.docs import Settings

class Settings(Settings):
    
    #Documentation:
    #http://sphinx-doc.org/config.html
    
    #Project
    
    project = 'run'
    author = 'roll'
    copyright = '2014, Respect31'
    version = run.version
    
    #Autodoc
    
    autodoc_member_order = 'bysource'
    autodoc_default_flags = ['members']
    
    
locals().update(Settings())