def fork(prototype, *args, **kwargs):
    """Fork attribute prototype with optional args, kwargs altering.
    """
    return prototype.__copy__(*args, **kwargs)