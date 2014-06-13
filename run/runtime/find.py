import os
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
                 file=None, basedir=None, recursively=False, **kwargs):
        self._names = names
        self._tags = tags
        if file == None:
            file = self.default_file
        if basedir == None:
            basedir = self.default_basedir 
        if os.path.sep not in file:
            maxdepth = 1
            if recursively:
                maxdepth = None
            kwargs.setdefault('filename', file)
            kwargs.setdefault('maxdepth', maxdepth)
        else:
            kwargs.setdefault('filepath', file)
        kwargs.setdefault('basedir', basedir)
        super().__init__(**kwargs)       
    
    #Protected

    _module_class = Module
    
    @property
    def _extension_mappers(self):
        return (super()._extension_mappers+
                [FindTypeMapper(self._module_class),
                 FindMetaMapper(self._names, self._tags)])
    
    
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
                    
                    
class FindMetaMapper:
    
    #Public
    
    def __init__(self, names, tags):
        self._names = names
        self._tags = tags
     
    def __call__(self, emitter):
        if self._names:
            if self._is_descriptor(emitter.object, 'meta_name'):
                emitter.skip()
            elif emitter.object.meta_name not in self._names:
                emitter.skip()
        if self._tags:
            if self._is_descriptor(emitter.object, 'meta_tags'):
                emitter.skip()
            elif set(emitter.object.meta_tags).isdisjoint(self._tags):
                emitter.skip()
        
    #Protected
    
    def _is_descriptor(self, obj, name):
        is_descriptor = False
        if inspect.isdatadescriptor(getattr(obj, name)):
            is_descriptor = True
            if name in vars(object):
                logging.getLogger(__name__).warning(
                    'Module class {obj} skipped because "{name}" '
                    'is not a static attribute (required for filter)'.
                    format(obj=obj, name=name))
        return is_descriptor