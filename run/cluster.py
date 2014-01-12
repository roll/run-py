import logging
from box.functools import cachedproperty
from .finder import Finder
from .settings import settings

class Cluster:

    #Public

    def __init__(self, names=[], tags=[], 
                 filename=None, basedir=None, recursively=False, 
                 existent=False, dispatcher=None):
        self._names = names
        self._tags = tags
        self._input_basedir = basedir
        self._input_filename = filename
        self._recursively = recursively
        self._existent = existent
        self._dispatcher = dispatcher
    
    def __getattr__(self, name):
        attributes = []
        for module in self._modules:
            try:
                attribute = getattr(module, name)
                attributes.append(attribute)
            except AttributeError as exception:
                if self._existent:
                    self._logger.warning(str(exception))
                else:
                    raise
        return attributes
        
    #Protected
    
    _finder_class = Finder
    _default_basedir = settings.default_basedir
    _default_filename = settings.default_file
        
    @cachedproperty
    def _modules(self):
        modules = []
        for module_class in self._module_classes:
            module = module_class(
                basedir=self._basedir, 
                dispatcher=self._dispatcher,
                module=None)
            modules.append(module)
        return modules
        
    @cachedproperty   
    def _module_classes(self):
        return list(self._module_finder.find(
            self._filename, self._basedir, self._recursively))
        
    @cachedproperty   
    def _module_finder(self):
        return self._finder_class(names=self._names, tags=self._tags)
    
    @property
    def _basedir(self):
        if self._input_basedir:
            return self._input_basedir
        else:
            return self._default_basedir
        
    @property
    def _filename(self):
        if self._input_filename:
            return self._input_filename
        else:
            return self._default_filename 
    
    @cachedproperty   
    def _logger(self):
        return logging.getLogger(__name__)        