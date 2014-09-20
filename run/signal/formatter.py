from box import terminal
from ..settings import settings


class Formatter:

    # Public

    def __init__(self, *, style, plain):
        self.__style = style
        self.__plain = plain

    def format(self, string, *, style=None, plain=None):
        if style is None:
            style = self.__style
        if plain is None:
            plain = self.__plain
        if not self.__plain:
            style = settings.styles.get(style, None)
            if style is not None:
                formater = terminal.Formatter()
                string = formater.format(string, **style)
        return string