import os
from box.findtools import find_objects
from box.functools import cachedproperty
from ..module import Module
from ..settings import settings
from .common import CommonConstraint
from .meta import MetaConstraint

from .not_found import NotFound

class find(find_objects):
    """Find run modules.
    """
    
    #Public
    
    default_basedir = settings.default_basedir
    default_exclude = settings.default_exclude    
    default_file = settings.default_file
    default_names = settings.default_names
    default_recursively = settings.default_recursively
    default_tags = settings.default_tags       
    
    def __init__(self, names=None, tags=None, *,
                 file=None, exclude=None, basedir=None, recursively=None, 
                 **kwargs):
        if names == None:
            names = self.default_names
        if tags == None:
            tags = self.default_tags                    
        if file == None:
            file = self.default_file
        if exclude == None:
            exclude = self.default_exclude  
        if basedir == None:
            basedir = self.default_basedir 
        if recursively == None:
            recursively = self.default_recursively 
        self._names = names
        self._tags = tags 
        if os.path.sep not in file:
            maxdepth = 1
            if recursively:
                maxdepth = None
            kwargs.setdefault('filename', file)
            kwargs.setdefault('maxdepth', maxdepth)
        else:
            kwargs.setdefault('filepath', file)          
        super().__init__(**kwargs)
    
    #Protected

    _getfirst_exception = NotFound
    _module_class = Module  
                
    @cachedproperty
    def _system_mappers(self):
        mappers = super()._system_mappers
        common = CommonConstraint(self._module_class)
        if common:
            mappers.append(common)
        meta = MetaConstraint(self._names, self._tags)
        if meta:
            mappers.appent(meta)
        return mappers      