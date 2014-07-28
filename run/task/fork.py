def fork(prototype, *args, **kwargs):
    """Fork task prototype with optional args, kwargs altering.

    Parameters
    ----------
    prototype: :class:`.TaskPrototype`
        Task prototype to fork.
    args: tuple
        Positional arguments to add to prototype's default.
    kwargs: dict
        Keyword arguments to add to prototype's default.

    Examples
    --------
    Usage example::

        class Module(Module):

            task1 = SomeTask()
            task2 = fork(attr1, meta_basedir='new/path', param='value')

    In this case task2 will build as task1 copy with redefined
    meta_basedir and default keyword argument param.
    """
    return prototype.__copy__(*args, **kwargs)
