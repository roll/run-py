def build(prototype, module):
    """Build prototype to module's attribute.

    Parameters
    ----------
    prototype: :class:`.AttributePrototype`
        Attribute prototype.
    module: :class:`.Module`
        Module to build prototype as attribute of module.

    Returns
    -------
    :class:`.Attribute`
        Builded attribute.
    """
    return prototype.__build__(module)
