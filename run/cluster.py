import logging
from lib31.python import cachedproperty
from .loader import Loader
from .settings import settings

class Cluster:

    #Public

    def __init__(self, names=[], tags=[], 
                 path=settings.default_path,
                 file_pattern=settings.default_file, 
                 recursively=False, 
                 existent=False):
        self._names = names
        self._tags = tags
        self._path = path
        self._file_pattern = file_pattern
        self._recursively = recursively
        self._existent = existent
    
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
            module = module_class(module=None)
            modules.append(module)
        return modules
        
    @cachedproperty   
    def _module_classes(self):
        return list(self._module_loader.load(
            self._path, self._file_pattern, self._recursively))
        
    @cachedproperty   
    def _module_loader(self):
        return self._loader_class(names=self._names, tags=self._tags)
    
    @cachedproperty   
    def _logger(self):
        return logging.getLogger(__name__)  