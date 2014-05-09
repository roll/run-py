import inspect
import logging
from box.findtools import find_objects
from ..module import Module
from ..settings import settings

class find(find_objects):
    
    #Public
    
    default_file = settings.default_file
    default_basedir = settings.default_basedir    
    
    def __init__(self, names=None, tags=None, *,
                 file=None, basedir=None, recursively=False, 
                 **kwargs):
        self._names = names
        self._tags = tags
        if file == None:
            file = self.default_file 
        if basedir == None:
            basedir = self.default_basedir 
        maxdepth = 1
        if recursively:
            maxdepth = None
        kwargs.setdefault('filename', file)
        kwargs.setdefault('basedir', basedir)
        kwargs.setdefault('maxdepth', maxdepth)
        super().__init__(**kwargs)       
    
    #Protected

    _module_class = Module
    
    @property
    def _extension_mappers(self):
        return (super()._extension_mappers+
                [FindTypeMapper(self._module_class),
                 FindMetaNameMapper(self._names),
                 FindMetaTagMapper(self._tags),])
    
    
class FindTypeMapper:
    
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
    
        
class FindMetaNameMapper:
    
    #Public
    
    def __init__(self, meta_names):
        self._meta_names = meta_names
        
    def __call__(self, emitter):
        if self._meta_names:
            if inspect.isdatadescriptor(emitter.object.meta_name):
                if 'meta_name' in vars(emitter.object):
                    logging.getLogger(__name__).warning(
                        'Module class {object} skipped because meta_name '
                        'is not a static attribute (required for name filter)'.
                        format(object=emitter.object))
                emitter.skip()
            else:            
                if emitter.object.meta_name not in self._meta_names:
                    emitter.skip()                 
    
    
class FindMetaTagMapper:
    
    #Public
    
    def __init__(self, meta_tags):
        self._meta_tags = meta_tags
        
    def __call__(self, emitter):
        if self._meta_tags:
            if inspect.isdatadescriptor(emitter.object.meta_tags):
                if 'meta_tags' in vars(emitter.object):
                    logging.getLogger(__name__).warning(
                        'Module class {object} skipped because meta_tags '
                        'is not a static attribute (required for tag filter)'.
                        format(object=emitter.object))
                emitter.skip()
            else:
                object_tags = set(emitter.object.meta_tags)
                filter_tags = set(self._meta_tags)
                if set.isdisjoint(object_tags, filter_tags):
                    emitter.skip()