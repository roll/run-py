import os
import inspect
from ...module import Module
from ...settings import settings  # @UnusedImport
from .find_modules import find_modules


class FindModule(Module):

    # Public

    @classmethod
    def __create__(cls, meta_module, meta_updates,
                   filename=settings.filename, key=None, tags=None,
                   basedir=None, **params):
        notfilepath = os.path.relpath(
            inspect.getfile(type(meta_module)), start=basedir)
        FoundModule = find_modules(
            filename=filename,
            key=key,
            tags=tags,
            filters=[{'notfilepath': notfilepath}],
            getfirst=True,
            **params)
        found_module = FoundModule(
            meta_module=meta_module,
            meta_updates=meta_updates)
        return found_module
