def fetch(module, name, *, category=None, resolve=True):
    """Return attribute by given name.
     
    .. seealso: It's a shortcut to :func:`run.module.Module.__getattribute__`
     """
    return module.__getattribute__(name, category=category, resolve=resolve)