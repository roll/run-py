import logging
from lib31.python import cachedproperty
from .loader import Loader
from .settings import settings

class Cluster:

    #Public

    #TODO: refactor defaults
    def __init__(self, names=[], tags=[], 
                 basedir=settings.default_basedir,
                 file_pattern=settings.default_file, 
                 recursively=False, 
                 existent=False,
                 dispatcher=None):
        self._names = names
        self._tags = tags
        self._basedir = basedir
        self._file_pattern = file_pattern
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
    
    _loader_class = Loader
        
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
        return list(self._module_loader.load(
            self._basedir, self._file_pattern, self._recursively))
        
    @cachedproperty   
    def _module_loader(self):
        return self._loader_class(names=self._names, tags=self._tags)
    
    @cachedproperty   
    def _logger(self):
        return logging.getLogger(__name__)  