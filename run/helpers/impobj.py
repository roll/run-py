import importlib


def import_object(name, *, package=None):
    """Import an object.

    Parameters
    ----------
    name: str/object
      Object name in "[module.]module.]attr" form.
    package: str
      Argument is required when performing a relative import.
      It specifies the package to use as the anchor point from which
      to resolve the relative import to an absolute import.

    Returns
    -------
    object
      Imported object.

    Raises
    ------
    ValueError
      If name is not in a proper form.
    ImportError
      If there is an error in module importing.
    AttributeError
      If module doesn't have the given attribute.

    Examples
    --------
    If name not is a string function returns name without changes.
    It usefull when client may give you pointer to some objects in
    two forms like string or already imported object::

      >>> obj = import_object('importlib.import_module')
      >>> obj is import_object(obj)
      True
      >>> obj
      <function importlib.import_module>
    """
    if isinstance(name, str):
        try:
            module, name = name.rsplit('.', 1)
        except ValueError:
            raise ValueError('Name is in a bad form.') from None
        if not module:
            module = '.'
        imported_module = importlib.import_module(module, package=package)
        imported_object = getattr(imported_module, name)
    else:
        imported_object = name
    return imported_object
