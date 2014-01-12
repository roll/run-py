import inspect
from box.findtools import find_objects
from .module import Module
from .settings import settings
    
class Finder:
    
    #Public
    
    def __init__(self, names=[], tags=[]):
        self._names = names
        self._tags = tags
        
    def find(self, filename, basedir=None, recursively=False):
        if not basedir:
            basedir = self._default_basedir
        if recursively:
            max_depth = None
        else:
            max_depth = 1
        filters = [
            FinderTypeFilter(self._module_class),
            FinderMetaNameFilter(self._names),
            FinderMetaTagFilter(self._tags),]
        modules = find_objects(filename=filename, 
            basedir=basedir, max_depth=max_depth, filters=filters)
        return modules
    
    #Protected

    _default_basedir = settings.default_basedir    
    _module_class = Module
    
    
class FinderTypeFilter:
    
    #Public
    
    def __init__(self, module_class):
        self._module_class = module_class
        
    def __call__(self, obj, name, module):
        if inspect.getmodule(obj) != module:
            return False
        if not isinstance(obj, type):
            return False
        if not issubclass(obj, self._module_class):
            return False
        if inspect.isabstract(obj):
            return False
        return True
    
    
class FinderMetaNameFilter:
    
    #Public
    
    def __init__(self, meta_names):
        self._meta_names = meta_names
        
    def __call__(self, obj, name, module):
        if self._meta_names:
            if obj.meta_name not in self._meta_names:
                return False
        return True
    
    
class FinderMetaTagFilter:
    
    #Public
    
    def __init__(self, meta_tags):
        self._meta_tags = meta_tags
        
    def __call__(self, obj, name, module):
        if self._meta_tags:
            object_tags = set(obj.meta_tags)
            filter_tags = set(self._meta_tags)
            if set.isdisjoint(object_tags, filter_tags):
                return False
        return True        