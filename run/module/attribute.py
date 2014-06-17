from ..attribute import Attribute; Attribute #PyDev warning bug

def attribute(module, name, *, category=Attribute, resolve=False):
    """Get attribute from module by given name.
    
    ..seealso It's shortcut for :func:`Module.__getattribute__`.
    """
    return module.__getattribute__(name, category=category, resolve=resolve)