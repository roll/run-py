import logging
from box.functools import cachedproperty
from ..settings import settings
from .find import find

class Cluster:

    #Public

    default_file = settings.default_file
    default_basedir = settings.default_basedir

    def __init__(self, names=None, tags=None, *, 
                 file=None, basedir=None, recursively=False, 
                 existent=False, dispatcher=None, **find_params):
        self._names = names
        self._tags = tags
        self._file = file
        self._basedir = basedir
        self._recursively = recursively
        self._existent = existent
        self._dispatcher = dispatcher
        self._find_params = find_params        
        if self._file == None:
            self._file = self.default_file
        if self._basedir == None:
            self._basedir = self.default_basedir                    
    
    def __getattr__(self, name):
        attributes = []
        for module in self._modules:
            try:
                attribute = getattr(module, name)
                attributes.append(attribute)
            except AttributeError as exception:
                if self._existent:
                    logger = logging.getLogger(__name__)
                    logger.warning(str(exception))
                else:
                    raise
        return attributes
        
    #Protected
    
    _find = staticmethod(find)
        
    @cachedproperty
    def _modules(self):
        modules = []
        module_classes = self._find(
            names=self._names, 
            tags=self._tags,
            file=self._file, 
            basedir=self._basedir, 
            recursively=self._recursively,
            **self._find_params)
        for module_class in module_classes:
            module = module_class(
                meta_dispatcher=self._dispatcher,
                meta_module=None)
            modules.append(module)
        return modules    