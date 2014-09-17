import os
import inspect
from ...module import Module
from .find_modules import find_modules


class FindModule(Module):

    # Public

    @classmethod
    def __meta_create__(cls, *args, meta_module, meta_updates,
                        key=None, tags=None,
                        file=None, exclude=None, basedir=None, recursively=None,
                        **kwargs):
        notfilepath = os.path.relpath(
            inspect.getfile(type(meta_module)), start=basedir)
        FoundModule = find_modules(
            target=Module,
            key=key,
            tags=tags,
            file=file,
            exclude=exclude,
            basedir=basedir,
            recursively=recursively,
            filters=[{'notfilepath': notfilepath}],
            getfirst=True)
        found_module = FoundModule(
            *args,
            meta_module=meta_module,
            meta_updates=meta_updates,
            **kwargs)
        return found_module
