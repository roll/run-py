import inspect
from copy import copy
from ..attribute import AttributePrototype, AttributeMetaclass, Attribute
from ..task import MethodTask
from ..var import ValueVar, DescriptorVar
from .prototype import ModulePrototype

class ModuleMetaclass(AttributeMetaclass):

    # Public

    def __new__(cls, name, bases, attrs):
        for key, attr in attrs.items():
            if key.isupper():
                continue
            if key.startswith('_'):
                continue
            if key.startswith('meta_'):
                continue
            if isinstance(attr, type):
                continue
            if isinstance(attr, cls._attribute_class):
                continue
            if isinstance(attr, cls._attribute_prototype_class):
                continue
            if isinstance(attr, staticmethod):
                continue
            if isinstance(attr, classmethod):
                continue
            if getattr(attr, '__isabstractmethod__', False):
                continue
            if getattr(attr, '__isskippedattribute__', False):
                continue
            if callable(attr):
                attrs[key] = cls._method_task_class(attr)
            elif inspect.isdatadescriptor(attr):
                attrs[key] = cls._descriptor_var_class(attr)
            else:
                attrs[key] = cls._value_var_class(attr)
        return super().__new__(cls, name, bases, attrs)

    def __copy__(self):
        attrs = {}
        for cls in self.mro():
            for key, attr in vars(cls).items():
                if (key not in attrs and
                    isinstance(attr, self._attribute_prototype_class)):
                    attrs[key] = copy(attr)
        attrs['__doc__'] = self.__doc__
        attrs['__module__'] = self.__module__
        return type(self)(self.__name__, (self,), attrs)

    # Protected

    _attribute_class = Attribute
    _attribute_prototype_class = AttributePrototype
    _descriptor_var_class = DescriptorVar
    _method_task_class = MethodTask
    _prototype_class = ModulePrototype
    _value_var_class = ValueVar
