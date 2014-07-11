import inspect
import logging

class MetaConstraint:
    
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