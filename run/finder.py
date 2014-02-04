import inspect
import logging
from box.functools import cachedproperty
from box.findtools import find_objects
from .module import Module
from .settings import settings
    
class Finder:
    
    #Public
    
    default_basedir = settings.default_basedir   
    
    def __init__(self, names=[], tags=[]):
        self._names = names
        self._tags = tags
        
    def find(self, filename, basedir=None, recursively=False):
        if not basedir:
            basedir = self.default_basedir
        if recursively:
            max_depth = None
        else:
            max_depth = 1
        mappers = [
            FinderTypeMapper(self._module_class),
            FinderMetaNameMapper(self._names),
            FinderMetaTagMapper(self._tags),]
        modules = find_objects(filename=filename, 
            basedir=basedir, max_depth=max_depth, mappers=mappers)
        return modules
    
    #Protected

    _module_class = Module
    
    
class FinderTypeMapper:
    
    #Public
    
    def __init__(self, module_class):
        self._module_class = module_class
        
    def __call__(self, emitter):
        if inspect.getmodule(emitter.object) != emitter.module:
            emitter.skip()
        elif not isinstance(emitter.object, type):
            emitter.skip()
        elif not issubclass(emitter.object, self._module_class):
            emitter.skip()
        elif inspect.isabstract(emitter.object):
            emitter.skip()
    
    
class FinderMetaNameMapper:
    
    #Public
    
    def __init__(self, meta_names):
        self._meta_names = meta_names
        
    def __call__(self, emitter):
        if self._meta_names:
            if emitter.object.meta_name not in self._meta_names:
                emitter.skip()
    
    
class FinderMetaTagMapper:
    
    #Public
    
    def __init__(self, meta_tags):
        self._meta_tags = meta_tags
        
    def __call__(self, emitter):
        if self._meta_tags:
            if inspect.isdatadescriptor(emitter.object.meta_tags):
                if 'meta_tags' in vars(emitter.object):
                    self._logger.warning(
                        'Module class {object} skipped because meta_tags '
                        'is not a static attribute (required for tags filter)'.
                        format(object=emitter.object))
                emitter.skip()
            else:
                object_tags = set(emitter.object.meta_tags)
                filter_tags = set(self._meta_tags)
                if set.isdisjoint(object_tags, filter_tags):
                    emitter.skip()
    
    #Protected
    
    _logging_module = logging
                
    @cachedproperty
    def _logger(self):
        return self._logging_module.getLogger(__name__)