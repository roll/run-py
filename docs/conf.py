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
    
    
locals().update(Settings())