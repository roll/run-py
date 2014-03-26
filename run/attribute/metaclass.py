from abc import ABCMeta
from .builder import build
from .draft import AttributeDraft

class AttributeMetaclass(ABCMeta):
    
    #Public
    
    def __call__(self, *args, **kwargs):
        build = kwargs.pop('build', False)
        draft = self._draft_class(self, *args, **kwargs)
        if build:
            return self._build_function(draft)
        else:
            return draft
        
    #Protected
    
    _draft_class = AttributeDraft
    _build_function = staticmethod(build)