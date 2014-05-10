from copy import copy as base_copy
from .prototype import AttributePrototype

def copy(prototype, *args, **kwargs):
    """Copy prototype with optional args, kwargs altering.
    
    For other types works as copy.copy.
    """
    if isinstance(prototype, AttributePrototype):
        return prototype.__copy__(*args, **kwargs)
    else:
        return base_copy(prototype)