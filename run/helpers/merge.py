from copy import copy
from .function import Function


class merge_dicts(Function):
    """Merge dicts with optional conflict resolving and return a new one.

    Parameters
    ----------
    dict1: dict
        Left dict to merge.
    dict2: dict
        Right dict to merge.
    resolvers: dict
        Conflict resolvers. Key is a type, value is a merge_dicts subclass
        or callable with [(value1, value2) -> value] signature.
        To make function recursive pass {dict: merge_dicts}.
        Resolvers parameter will be passed resursively to
        any merge_dicts subclass resolver.

    Returns
    -------
    dict
        Merged dict.

    Examples
    --------
    Here is the code::

        >>> from operators import add
        >>> dict1 = {'a': 1, 'b': 2}
        >>> dict2 = {'a': 1, 'c': 3}
        >>> merge_dicts(dict1, dict2, resolvers={int: add})
        {'a': 2, 'b': 2, 'c', 3}
    """

    protocol = 'function'

    def __call__(self, dict1, dict2, *, resolvers={}):
        result = copy(dict1)
        for key in dict2:
            value = dict2[key]
            if key in dict1:
                resolver1 = resolvers.get(type(dict1[key]), None)
                resolver2 = resolvers.get(type(dict2[key]), None)
                if resolver1 is resolver2 is not None:
                    if (not isinstance(resolver1, type) or
                        not issubclass(resolver1, merge_dicts)):
                        value = resolver1(dict1[key], dict2[key])
                    else:
                        value = resolver1(
                            dict1[key], dict2[key], resolvers=resolvers)
            result[key] = value
        return result
