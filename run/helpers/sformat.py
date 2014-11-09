import clyde


def sformat(string, style=None, styles={}):
    if not isinstance(style, dict):
        style = styles.get(style, None)
    if style is not None:
        string = clyde.sformat(string, **style)
    return string
