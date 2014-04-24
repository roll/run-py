from box.importlib import import_object
from ..attribute import Attribute

class ModuleAttributes(dict):

    #Public

    def __init__(self, module):
        self._module = module
        for name, attr in vars(type(module)).items():
            if isinstance(attr, Attribute):
                self[name] = attr
                
    def get_attribute(self, name, *, category=Attribute, resolve=False):
        """Return attribute by given name.
        
        :param str name: attribute name, supports nested like "module.attribute"
        :param None/type/str category: returns attribute only of given class
        :param bool resolve: if True resolves attribute and returns value
        
        :raises AttributeError: if module has not attribute for given name
        :raises TypeError: if attribute is not instance of given category
        :raises TypeError: if in nested name first attribute is not a Module
        
        :return: attribute instance/attribute value
        :rtype: :class:`run.Attribute`/mixed
        """
        try:
            name, nested_name = name.split('.', 1)
        except ValueError:
            nested_name = None
        try:
            attribute = self[name]
        except KeyError:
            raise AttributeError(
            'Module "{module}" has no attribute "{name}".'.
            format(module=self._module, name=name)) from None
        if category:
            category = import_object(category)
            if not isinstance(attribute, category):
                raise TypeError(
                    'Attribute "{name}" is not a "{category}".'.
                    format(name=name, category=category))
        if nested_name:
            from .module import Module
            if not isinstance(attribute, Module):
                raise TypeError(
                    'Attribute "{name}" is not a Module.'.
                    format(attribute=attribute))
            return attribute.meta_attributes.get_attribute(
                nested_name, category=category, resolve=resolve)
        if resolve:
            return attribute.__get__(attribute.meta_module)
        return attribute  