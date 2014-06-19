def attribute(module, name, *, category=None, getvalue=True):
    """Return attribute by given name.
     
    .. seealso:: It's a shortcut to :func:`run.module.Module.__getattribute__`
    """
    return module.__getattribute__(name, category=category, getvalue=getvalue)