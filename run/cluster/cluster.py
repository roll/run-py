import logging
from box.functools import cachedproperty
from .find_files import find_files
from .find_modules import find_modules

class Cluster:
    """Modules cluster representation.
    """

    #Public

    def __init__(self, names=None, tags=None, *, 
                 file=None, basedir=None, recursively=False, 
                 existent=False, dispatcher=None):
        self._names = names
        self._tags = tags
        self._file = file
        self._basedir = basedir
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
                if not self._existent:
                    raise
                else:
                    logger = logging.getLogger(__name__)
                    logger.warning(str(exception))   
        return attributes
        
    #Protected
    
    _find_files = staticmethod(find_files)
    _find_modules = staticmethod(find_modules)
        
    @cachedproperty
    def _modules(self):
        modules = []
        for module_class in self._module_classes:
            module = module_class(
                meta_dispatcher=self._dispatcher,
                meta_module=None)
            modules.append(module)
        return modules
    
    @cachedproperty
    def _module_classes(self):
        module_classes = self._find_modules(
            names=self._names, 
            tags=self._tags,
            files=self._files)
        return module_classes
    
    @cachedproperty    
    def _files(self):
        files = self._find_files(
            file=self._file, 
            basedir=self._basedir, 
            recursively=self._recursively,
            join=True)
        return files