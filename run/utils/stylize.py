import sugarbowl
from ..settings import settings


def stylize(string, *, style, **patch):
    """Format string with style.
    """
    if not settings.plain:
        if not isinstance(style, dict):
            style = settings.styles.get(style, {})
        style.update(patch)
        string = sugarbowl.stylize(string, **style)
    return string
