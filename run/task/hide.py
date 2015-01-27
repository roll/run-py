from .convert import convert


def hide(obj):
    """Convert object to hidden task.
    """
    converted_object = convert(obj, Hidden=True)
    return converted_object
