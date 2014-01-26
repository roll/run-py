from ..attribute import Attribute

class ModuleAttributes(dict):

    #Public

    def __init__(self, module):
        self._module = module
        for name, attr in vars(type(module)).items():
            if isinstance(attr, Attribute):
                self[name] = attr