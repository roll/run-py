import sugarbowl
from ..settings import settings


def stylize(self, string, *, styles, modes={}, layers={}, colors={}, **style):
    """Format string with style.
    """
    if not settings.plain:
        estyle = {}
        for item in styles:
            item = settings.styles.get(item, None)
            if item is not None:
                estyle.update(item)
        estyle.update(style)
        string = sugarbowl.stylize(
            string, modes=modes, layers=layers, colors=colors, **estyle)
    return string
