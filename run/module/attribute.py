def attribute(module, name, *, category=None, getvalue=True):
    """Return module's attribute by given name.
     
    .. seealso:: It's a shortcut to :attr:`run.module.Module.__getattribute__`
    """
    return module.__getattribute__(name, category=category, getvalue=getvalue)