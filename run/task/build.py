def build(prototype, module):
    """Build task prototype to module's task.

    Parameters
    ----------
    prototype: :class:`.TaskPrototype`
        Task prototype.
    module: :class:`.Module`
        Module to build prototype as task of module.

    Returns
    -------
    :class:`.Task`
        Builded task.
    """
    return prototype.__build__(module)
