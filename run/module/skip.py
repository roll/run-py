def skip(attribute):
    setattr(attribute, '__isskippedattribute__', True)
    return attribute