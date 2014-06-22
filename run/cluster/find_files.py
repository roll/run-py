import os
from box.findtools import find_files
from ..settings import settings
from .not_found import NotFound

class find_files(find_files):
    """Find run files.
    """
    
    #Public
    
    default_file = settings.default_file
    default_basedir = settings.default_basedir    
    
    def __init__(self, file=None, *,
                 basedir=None, recursively=False, **kwargs):
        if file == None:
            file = self.default_file
        if basedir == None:
            basedir = self.default_basedir 
        if os.path.sep not in file:
            maxdepth = 1
            if recursively:
                maxdepth = None
            kwargs.setdefault('filename', file)
            kwargs.setdefault('maxdepth', maxdepth)
        else:
            kwargs.setdefault('filepath', file)
        super().__init__(basedir=basedir, **kwargs)
        
    #Protected
    
    _getfirst_exception = NotFound