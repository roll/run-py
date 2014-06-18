from box.importlib import import_object
from ..attribute import Attribute; Attribute #PyDev warning bug
 
def fetch(module, name, *, category=Attribute, resolve=False):
    """Return attribute by given name.
     
    :param object module: module instance
    :param str name: attribute name, supports nested like "module.attribute"
    :param None/type/str category: returns attribute only of given class
    :param bool resolve: if True resolves attribute and returns value
    
    :raises TypeError: if module is not a Module
    :raises AttributeError: if module has not attribute for given name
    :raises TypeError: if attribute is not instance of given category
    
    :returns: attribute instance/attribute value
    :rtype: :class:`run.attribute.Attribute`/mixed
     """
    from .module import Module
    if not isinstance(module, Module):
        raise TypeError(
            'Argument "{argument}" is not a Module.'.
            format(argument=module))
    try:
        name, nested_name = name.split('.', 1)
    except ValueError:
        nested_name = None
    try:
        attribute = module.meta_attributes[name]
    except KeyError:
        raise AttributeError(
        'Module "{module}" has no attribute "{name}".'.
        format(module=module, name=name)) from None
    if nested_name:
        return fetch(attribute, nested_name, 
            category=category, resolve=resolve)
    if category:
        category = import_object(category)
        if not isinstance(attribute, category):
            raise TypeError(
                'Attribute "{name}" is not a {category}.'.
                format(name=name, category=category))
    if resolve:
        return attribute.__get__(attribute.meta_module)
    return attribute 