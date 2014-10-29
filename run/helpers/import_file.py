import os
from importlib.machinery import SourceFileLoader


def import_file(filepath):
    """Import module from file by filepath.

    Parameters
    ----------
    filepath: str
        Module filepath.

    Returns
    -------
    object
        Imported module.
    """
    filepath = os.path.abspath(filepath)
    loader = SourceFileLoader(filepath, filepath)
    # Method load_module is deprecated since Python 3.4
    # New API is not clear before Python 3.5
    module = loader.load_module(filepath)
    return module
