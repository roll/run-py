import os
import inspect
from pprint import pprint
from collections import OrderedDict
from ..attribute import Attribute
from ..task import Task, NullTask
from .error import ModuleAttributeError
from .metaclass import ModuleMetaclass

class Module(Attribute, metaclass=ModuleMetaclass):

    # Public

    def __get__(self, module=None, module_class=None):
        return self

    def __set__(self, module, value):
        raise AttributeError(
            'Attribute is module "{module}" '
            'and can\'t be set to any value'.
            format(module=self))

    def __call__(self, *args, **kwargs):
        return self.default(*args, **kwargs)

    def __getattribute__(self, name):
        nested_name = None
        if '.' in name:
            name, nested_name = name.split('.', 1)
        try:
            attribute = super().__getattribute__(name)
        except AttributeError as exception:
            # To get correct attribute error message here
            if isinstance(exception, ModuleAttributeError):
                raise
            raise ModuleAttributeError(
                'Module "{module}" has no attribute "{name}".'.
                format(module=self, name=name))
        if nested_name is not None:
            attribute = getattr(attribute, nested_name)
        return attribute

    @property
    def meta_attributes(self):
        """Module's attributes dict-like object.

        Dict contains attribute instances, not values.
        """
        attributes = {}
        for name, attr in vars(type(self)).items():
            if isinstance(attr, Attribute):
                attributes[name] = attr
        return attributes

    @property
    def meta_basedir(self):
        """Module's basedir.

        Define default meta_basedir for all attributes.

        This property is:

        - initable/writable
        - inherited from module
        """
        if self.meta_is_main_module:
            basedir = os.path.dirname(inspect.getfile(type(self)))
        else:
            basedir = self.meta_module.meta_basedir
        return self._meta_params.get('basedir', basedir)

    @meta_basedir.setter
    def meta_basedir(self, value):
        self._meta_params['basedir'] = value

    @property
    def meta_cache(self):
        """Module's caching status (enabled or disabled).

        Define default meta_cache for all attributes.

        This property is:

        - initable/writable
        - inherited from module
        """
        return self._meta_params.get('cache',
            self.meta_module.meta_cache)

    @meta_cache.setter
    def meta_cache(self, value):
        self._meta_params['cache'] = value

    @property
    def meta_chdir(self):
        """Module's chdir status (enabled or disabled).

        Define default meta_chdir for all attributes.

        This property is:

        - initable/writable
        - inherited from module
        """
        return self._meta_params.get('chdir',
            self.meta_module.meta_chdir)

    @meta_chdir.setter
    def meta_chdir(self, value):
        self._meta_params['chdir'] = value

    @property
    def meta_fallback(self):
        """Module's fallback.

        Define default meta_fallback for all attributes.

        This property is:

        - initable/writable
        - inherited from module
        """
        return self._meta_params.get('fallback',
            self.meta_module.meta_fallback)

    @meta_fallback.setter
    def meta_fallback(self, value):
        self._meta_params['fallback'] = value

    @property
    def meta_is_main_module(self):
        """Module's main module status (is main module or not).
        """
        if self.meta_module:
            return False
        else:
            return True

    @property
    def meta_main_module(self):
        if self.meta_is_main_module:
            return self
        else:
            return self.meta_module.meta_main_module

    @property
    def meta_name(self):
        if super().meta_name:
            return super().meta_name
        else:
            return self._default_meta_main_module_name

    @property
    def meta_strict(self):
        """Module's strict mode status (enabled or disabled).

        Define default meta_strict for all attributes.

        This property is:

        - initable/writable
        - inherited from module
        """
        return self._meta_params.get('strict',
            self.meta_module.meta_strict)

    @meta_strict.setter
    def meta_strict(self, value):
        self._meta_params['strict'] = value

    @property
    def meta_tags(self):
        """Module's tag list.
        """
        return []

    def list(self, attribute=None):
        """Print attributes.
        """
        if attribute != None:
            attribute = getattr(self, attribute)
        else:
            attribute = self
        names = []
        if isinstance(attribute, Module):
            for attribute in attribute.meta_attributes.values():
                names.append(attribute.meta_qualname)
            for name in sorted(names):
                self._print(name)
        else:
            raise TypeError(
                'Attribute "{attribute}" is not a module.'.
                format(attribute=attribute))

    def info(self, attribute=None):
        """Print information.
        """
        if attribute != None:
            attribute = getattr(self, attribute)
        else:
            attribute = self
        info = attribute.meta_qualname
        if isinstance(attribute, Task):
            info += attribute.meta_signature
        info += '\n---\n'
        info += 'Type: ' + attribute.meta_type
        if isinstance(attribute, Task):
            info += '\n'
            info += 'Dependencies: ' + str(attribute.meta_dependencies)
            info += '\n'
            info += 'Default arguments: ' + str(attribute.meta_args)
            info += '\n'
            info += 'Default keyword arguments: ' + str(attribute.meta_kwargs)
        info += '\n---\n'
        info += attribute.meta_docstring
        self._print(info)

    def meta(self, attribute=None):
        """Print metadata.
        """
        if attribute != None:
            attribute = getattr(self, attribute)
        else:
            attribute = self
        meta = OrderedDict()
        for name in sorted(dir(attribute)):
            if name.startswith('meta_'):
                key = name.replace('meta_', '')
                meta[key] = getattr(attribute, name)
        self._pprint(meta)

    default = NullTask(
        meta_require=['list'],
    )

    # Protected

    _print = staticmethod(print)
    _pprint = staticmethod(pprint)
