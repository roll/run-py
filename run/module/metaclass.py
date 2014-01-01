import inspect
from ..attribute import AttributeBuilder, AttributeMetaclass, Attribute
from ..task import MethodTask
from ..var import ValueVar, PropertyVar
from .builder import ModuleBuilder

class ModuleMetaclass(AttributeMetaclass):
     
    #Public
     
    def __new__(cls, name, bases, dct):
        for key, attr in dct.items():
            if key.startswith('_'):
                continue
            elif key.startswith('meta_'):
                continue
            elif isinstance(attr, type):
                continue
            elif isinstance(attr, cls._attribute_class):
                continue
            elif isinstance(attr, cls._attribute_builder_class):
                continue
            elif callable(attr):
                dct[key] = cls._method_task_class(attr)
            elif inspect.isdatadescriptor(attr):
                dct[key] = cls._property_var_class(attr)
            else:
                dct[key] = cls._value_var_class(attr)
        return super().__new__(cls, name, bases, dct)
    
    #Protected
    
    _builder_class = ModuleBuilder
    
    _attribute_class = Attribute
    _attribute_builder_class = AttributeBuilder
    _method_task_class = MethodTask
    _property_var_class = PropertyVar
    _value_var_class = ValueVar