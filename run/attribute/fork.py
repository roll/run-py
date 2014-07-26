def fork(prototype, *args, **kwargs):
    """Fork attribute prototype with optional args, kwargs altering.

    Parameters
    ----------
    prototype: :class:`.AttributePrototype`
        Attribute prototype to fork.
    args: tuple
        Positional arguments to add to prototype's default.
    kwargs: dict
        Keyword arguments to add to prototype's default.

    Examples
    --------
    Usage example::

        class Module(Module):

            attr1 = SomeTask()
            attr2 = fork(attr1, meta_basedir='new/path', param='value')

    In this case attr2 will build as attr1 copy with redefined
    meta_basedir and default keyword argument param.
    """
    return prototype.__copy__(*args, **kwargs)
