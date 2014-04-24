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
        
        Supports nested names like "module.attribute". 
        If resolve is True returns attribute value. 
        
        :raise AttributeError: if module has not attribute for given name
        :raise TypeError: if attribute is not instance of given category
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
            if not isinstance(attribute, category):
                raise TypeError(
                    'Attribute "{name}" is not a "{category}".'.
                    format(name=name, category=category))
        if nested_name:
            #TODO: add is Module check? 
            return attribute.meta_attributes.get_attribute(
                nested_name, category=category, resolve=resolve)                
        if resolve:
            return attribute.__get__(attribute.meta_module)
        return attribute  