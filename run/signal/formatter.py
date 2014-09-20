from box import terminal
from ..settings import settings


class Formatter:

    # Public

    def __init__(self, *, plain):
        self.__plain = plain

    def format(self, string, *, style):
        if not self.__plain:
            style = settings.styles.get(style, None)
            if style is not None:
                formater = terminal.Formatter()
                string = formater.format(string, **style)
        return string