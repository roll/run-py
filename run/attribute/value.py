def value(attribute):
    """Return attribute's value.
    """
    return attribute.__get__(attribute.meta_module)
