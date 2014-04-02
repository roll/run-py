import logging
from box.functools import cachedproperty
from .finder import Finder
from .settings import settings

class Cluster:

    #Public

    default_filename = settings.default_file
    default_basedir = settings.default_basedir

    def __init__(self, names=[], tags=[], 
                 filename=None, basedir=None, recursively=False, 
                 existent=False, dispatcher=None):
        self._names = names
        self._tags = tags
        self._filename = filename
        self._basedir = basedir
        self._recursively = recursively
        self._existent = existent
        self._dispatcher = dispatcher
        if not self._filename:
            self._filename = self.default_filename
        if not self._basedir:
            self._basedir = self.default_basedir                    
    
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
        
    @cachedproperty
    def _modules(self):
        modules = []
        for module_class in self._module_classes:
            module = module_class(
                meta_basedir=self._basedir, 
                meta_dispatcher=self._dispatcher,
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
    
    @cachedproperty   
    def _logger(self):
        return logging.getLogger(__name__)        