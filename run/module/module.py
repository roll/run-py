from pprint import pprint
from collections import OrderedDict
from ..task import NullTask
from .base import BaseModule

class Module(BaseModule):
    
    #Public
        
    def list(self, attribute=None):
        "Print attributes"
        names = []
        if attribute and attribute in self.meta_attributes:
            attribute = self.meta_attributes[attribute]
            attributes = attribute.meta_attributes
        else:
            attributes = self.meta_attributes
        for attribute in attributes.values():
            names.append(attribute.meta_qualname)
        for name in sorted(names):
            self._meta_print_operator(name)

    def info(self, attribute=None):
        "Print information"
        if attribute and attribute in self.meta_attributes:
            attribute = self.meta_attributes[attribute]
            self._meta_print_operator(attribute.meta_info)
        else:
            self._meta_print_operator(self.meta_info)
        
    def meta(self, attribute=None):
        "Print metadata"
        if attribute and attribute in self.meta_attributes:
            attribute = self.meta_attributes[attribute]
        else:
            attribute = self
        meta = OrderedDict()
        for name in sorted(dir(attribute)):
            if name.startswith('meta_'):
                key = name.replace('meta_', '')
                meta[key] = getattr(attribute, name)
        self._meta_formatted_print_operator(meta)
      
    default = NullTask(
        require=['list'],
    )
    
    #Protected
    
    _meta_formatted_print_operator = staticmethod(pprint)
    _meta_print_operator = staticmethod(print)