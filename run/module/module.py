from pprint import pprint
from collections import OrderedDict
from ..task import NullTask
from .base import BaseModule

class Module(BaseModule):
    
    #Public
        
    def list(self, attribute=None):
        "Print attributes"
        if attribute:
            attribute = self.meta_attributes[attribute]
        else:
            attribute = self
        names = []
        if isinstance(attribute, BaseModule):
            for attribute in attribute.meta_attributes.values():
                names.append(attribute.meta_qualname)
            for name in sorted(names):
                self._meta_print_function(name)
        else:
            raise TypeError(
                'Attribute "{attribute}" is not a module.'.
                format(attribute=attribute))

    def info(self, attribute=None):
        "Print information"
        if attribute:
            attribute = self.meta_attributes[attribute]
        else:
            attribute = self
        self._meta_print_function(attribute.meta_info)
        
    def meta(self, attribute=None):
        "Print metadata"
        if attribute:
            attribute = self.meta_attributes[attribute]
        else:
            attribute = self
        meta = OrderedDict()
        for name in sorted(dir(attribute)):
            if name.startswith('meta_'):
                key = name.replace('meta_', '')
                meta[key] = getattr(attribute, name)
        self._meta_pprint_function(meta)
      
    default = NullTask(
        require=['list'],
    )
    
    #Protected
    
    _meta_print_function = staticmethod(print)    
    _meta_pprint_function = staticmethod(pprint)