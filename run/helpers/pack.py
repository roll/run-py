def pack(*args, **kwargs):
    """Pack args, kwargs to a string.
    """
    result = ''
    if args or kwargs:
        result += '('
        elements = []
        for value in args:
            element = repr(value)
            elements.append(element)
        for key, value in kwargs.items():
            element = '{0}={1}'.format(str(key), repr(value))
            elements.append(element)
        result += ', '.join(elements)
        result += ')'
    return result