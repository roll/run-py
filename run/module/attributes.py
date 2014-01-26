from ..attribute import Attribute

class ModuleAttributes(dict):

    #Public

    def __init__(self, module):
        self._module = module
        for name, attr in vars(type(module)).items():
            if isinstance(attr, Attribute):
                self[name] = attr
                
    def __getitem__(self, key):
        if '.' in key:
            module_name, attribute_name = key.split('.', 1)
            module = self.get(module_name, None)
            module_attributes = getattr(module, 'meta_attributes', None)
            if isinstance(module_attributes, type(self)):
                attribute = module_attributes[attribute_name]
                return attribute
        return super().__getitem__(key)