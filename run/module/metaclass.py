import inspect
from ..attribute import AttributeBuilder, AttributeMetaclass, Attribute
from ..task import MethodTask
from ..var import ValueVar, PropertyVar
from .builder import ModuleBuilder

class ModuleMetaclass(AttributeMetaclass):
     
    #Public
     
    def __new__(cls, name, bases, dct):
        for key, attr in dct.items():
            if (not key.startswith('_') and
                not key.startswith('meta_') and
                not isinstance(attr, type) and
                not isinstance(attr, Attribute) and
                not isinstance(attr, AttributeBuilder)):
                if callable(attr):
                    dct[key] = MethodTask(attr)
                elif inspect.isdatadescriptor(attr):
                    dct[key] = PropertyVar(attr)
                else:
                    dct[key] = ValueVar(attr)
        return super().__new__(cls, name, bases, dct)
    
    #Protected
    
    _builder_class = ModuleBuilder