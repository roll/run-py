import ast
import csv


def parse(string):
    """Parse args, kwargs call representation.

    Parameters
    ----------
    string: str
        String to parse.

    Returns
    -------
    tuple
        (args, kwargs)
    """
    args = []
    kwargs = {}
    elements = next(csv.reader([string], quotechar='\\'))
    for element in elements:
        parts = []
        literals = next(csv.reader(
            [element], delimiter='=', quotechar='\\'))
        for literal in literals:
            literal = literal.strip()
            try:
                value = ast.literal_eval(literal)
            except Exception:
                value = literal
            parts.append(value)
        if len(parts) == 1:
            args.append(parts[0])
        elif len(parts) == 2:
            kwargs[parts[0]] = parts[1]
    args = tuple(args)
    return (args, kwargs)
