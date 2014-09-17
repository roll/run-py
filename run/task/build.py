def build(prototype, module):
    """Build task prototype to module's task.

    Parameters
    ----------
    prototype: :class:`.Prototype`
        Task prototype.
    module: :class:`.Module`
        Module to build prototype as task of module.

    Returns
    -------
    :class:`.Task`
        Builded task.
    """
    return prototype.__meta_build__(module)
