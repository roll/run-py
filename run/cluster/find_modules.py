import inspect
import logging
from box.findtools import find_objects
from ..module import Module
from ..settings import settings
from .not_found import NotFound

class find_modules(find_objects):
    """Find run modules.
    """
    
    #Public
    
    default_basedir = settings.default_basedir    
    
    def __init__(self, names=None, tags=None, *,
                 files=[], basedir=None, **kwargs):
        self._names = names
        self._tags = tags
        if basedir == None:
            basedir = self.default_basedir        
        super().__init__(files=files, basedir=basedir, **kwargs)
    
    #Protected

    _getfirst_exception = NotFound
    _module_class = Module
    
    @property
    def _extension_mappers(self):
        return (super()._extension_mappers+
                [FindModulesTypeMapper(self._module_class),
                 FindModulesMetaMapper(self._names, self._tags)])
        
        
class FindModulesTypeMapper:
    
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
            
            
class FindModulesMetaMapper:
    
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