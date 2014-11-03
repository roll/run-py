from copy import copy as python_copy


def enhanced_copy(obj, *args, **kwargs):
    """Shallow copy operation on arbitrary Python objects.

    Difference with python library module is in __copy__ method priority:

      - if object has __copy__ method function calls it with args and kwarg
      - if object hasn't __copy__ method function acts like copy.copy

    Parameters
    ----------
    obj: mixed
        Object to copy.
    args: tuple
        Args to pass to object's __copy__ method.
    kwargs: dict
        Kwargs to pass to object's __copy__ method.

    Returns
    -------
    mixed
        Shallow copy of the object.
    """
    if hasattr(obj, '__copy__'):
        return obj.__copy__(*args, **kwargs)
    else:
        return python_copy(obj)
