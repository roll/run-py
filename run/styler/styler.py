from clyde import Styler
from ..settings import settings


class Styler(Styler):

    # Public

    def format(self, string, *, style):
        result = ''
        if not settings.plain:
            if not isinstance(style, dict):
                style = settings.styles.get(style, None)
            if style is not None:
                result = super().format(string, **style)
        return result
