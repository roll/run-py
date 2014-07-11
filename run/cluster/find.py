import os
from box.findtools import find_objects
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
        self._names = names
        self._tags = tags
        self._file = file
        self._exclude = exclude
        self._basedir = basedir
        self._recursively = recursively
        if self._names == None:
            self._names = self.default_names
        if self._tags == None:
            self._tags = self.default_tags                    
        if self._file == None:
            self._file = self.default_file
        if self._exclude == None:
            self._exclude = self.default_exclude  
        if self._basedir == None:
            self._basedir = self.default_basedir 
        if self._recursively == None:
            self._recursively = self.default_recursively            
        super().__init__(**kwargs)
    
    #Protected

    _getfirst_exception = NotFound
    _module_class = Module  
                
    @property
    def _system_mappers(self):
        mappers = super()._system_mappers
        common = CommonConstraint(self._module_class)
        if common:
            mappers.append(common)
        meta = MetaConstraint(self._names, self._tags)
        if meta:
            mappers.appent(meta)
        return mappers

    @property
    def _filename(self):
        if os.path.sep not in self._file:
            maxdepth = 1
            if self._recursively:
                maxdepth = None
            filename = self._file