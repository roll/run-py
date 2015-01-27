from .function import Function


class stylize(Function):
    """Format string with style.
    """

    # Public

    modes = {
        'bold': 1,
        'underline': 4,
    }

    layers = {
        'foreground': 30,
        'background': 40,
    }

    colors = {
        'black': 0,
        'red': 1,
        'green': 2,
        'yellow': 3,
        'blue': 4,
        'magenta': 5,
        'cyan': 6,
        'white': 7,
        'bright_black': 60,
        'bright_red': 61,
        'bright_green': 62,
        'bright_yellow': 63,
        'bright_blue': 64,
        'bright_magenta': 65,
        'bright_cyan': 66,
        'bright_white': 67,
    }

    def __init__(self, string, **style):
        self.__string = string
        self.__style = style

    def __call__(self):
        result = self.__string
        offsets = self.__make_offsets()
        if offsets:
            open_code = self.__make_code(offsets)
            close_code = self.__make_code([self.__reset_offset])
            result = open_code + result + close_code
        return result

    # Private

    __reset_offset = 0
    __begin_code = '\x1b['
    __sep_code = ';'
    __end_code = 'm'

    def __make_offsets(self):
        offsets = []
        for key, value in self.__style.items():
            try:
                if key in self.layers:
                    offset = self.layers[key] + self.colors[value]
                elif value:
                    offset = self.modes[key]
            except Exception:
                raise ValueError(
                    'Bad value "{value}" for key "{key}"'.
                    format(value=value, key=key))
            offsets.append(offset)
        return offsets

    def __make_code(self, offsets):
        style_code = self.__sep_code.join(map(str, sorted(offsets)))
        code = self.__begin_code + style_code + self.__end_code
        return code
