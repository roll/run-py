import inspect
from lib31.python import ObjectLoader
from .module import Module
    
class Loader(ObjectLoader):
    
    #Public
    
    def __init__(self, names=[], tags=[]):
        self._names = names
        self._tags = tags
    
    #Protected
    
    def _filter_object(self, obj, module, name):
        result = (super()._filter_object(obj, module, name) and
                  self._filter_object_by_type(obj, module) and
                  self._filter_object_by_name(obj) and
                  self._filter_object_by_tags(obj))
        return result
    
    def _filter_object_by_type(self, obj, module):
        if (inspect.getmodule(obj) != module or
            not isinstance(obj, type) or
            not issubclass(obj, Module) or
            inspect.isabstract(obj)):
            return False
        return True
    
    def _filter_object_by_name(self, obj):
        if self._names:
            if obj.meta_name not in self._names:
                return False
        return True
    
    def _filter_object_by_tags(self, obj):
        if self._tags:
            object_tags = set(obj.meta_tags)
            filter_tags = set(self._tags)
            if set.isdisjoint(object_tags, filter_tags):
                return False
        return True    