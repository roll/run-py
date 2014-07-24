import inspect
from abc import abstractmethod
from ..settings import settings
from .metaclass import AttributeMetaclass

class Attribute(metaclass=AttributeMetaclass):
    """Main base class for attributes.

    This class is abstract base class for every attribute
    used in run. Abstract methods: __get__, __set__.
    """

    # Public

    # TODO: we can't use module keyword in kwargs (also cls, updated?)
    def __build__(self, module, *args, **kwargs):
        self._meta_module = module
        self._meta_params = {}
        for key in list(kwargs):
            if key.startswith('meta_'):
                self._meta_params[key.lstrip('meta_')] = kwargs.pop(key)
        self.__init__(*args, **kwargs)
        self._meta_builded = True

    @abstractmethod
    def __get__(self, module, module_class=None):
        pass  # pragma: no cover

    @abstractmethod
    def __set__(self, module, value):
        pass  # pragma: no cover

    def __repr__(self):
        if self.meta_builded:
            return '<{category} "{qualname}">'.format(
                category=self.meta_type,
                qualname=self.meta_qualname)
        else:
            return super().__repr__()

    @property
    def meta_builded(self):
        """Build status of attribute (builded or not).

        Attribute is builded after succefull __build__ call.
        It includes some internal building and __init__ call.
        """
        return vars(self).get('_meta_builded', False)

    @property
    def meta_dispatcher(self):
        """Attribute's dispatcher.

        Dispatcher used to operate signals.

        This property is:

        - initable/writable
        - inherited from module
        """
        return self._meta_params.get('dispatcher',
            self.meta_module.meta_dispatcher)

    @meta_dispatcher.setter
    def meta_dispatcher(self, value):
        self._meta_params['dispatcher'] = value

    @property
    def meta_docstring(self):
        """Attribute's docstring.

        This property is:

        - initable/writable
        """
        return self._meta_params.get('docstring',
            str(inspect.getdoc(self)).strip())

    @meta_docstring.setter
    def meta_docstring(self, value):
        self._meta_params['docstring'] = value

    @property
    def meta_main_module(self):
        """Attribute's main module of module hierarchy.
        """
        return self.meta_module.meta_main_module

    @property
    def meta_module(self):
        """Attribute's module.
        """
        return self._meta_module

    @property
    def meta_name(self):
        """Attribute's name.

        Name is defined as attribute name in module.
        If module is None name will be empty string.
        """
        name = ''
        attributes = self.meta_module.meta_attributes
        for key, attribute in attributes.items():
            if attribute is self:
                name = key
        return name

    @property
    def meta_qualname(self):
        """Attribute's qualified name.

        Qualname is full attribute name in hierarhy
        starts from main module.
        """
        if self.meta_module.meta_is_main_module:
            if (self.meta_module.meta_name ==
                self._default_meta_main_module_name):
                pattern = '{name}'
            else:
                pattern = '[{module_qualname}] {name}'
        else:
            pattern = '{module_qualname}.{name}'
        return pattern.format(
            module_qualname=self.meta_module.meta_qualname,
            name=self.meta_name)

    @property
    def meta_type(self):
        """Attribute's type as a string.
        """
        return type(self).__name__

    # Protected

    _default_meta_main_module_name = settings.default_meta_main_module_name
