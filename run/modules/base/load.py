from ...module import ModuleLoader
from ...settings import settings

class LoadModule:

    #Public

    #TODO: error handling
    def __new__(self, names=[], tags=[],
                 base_dir=settings.default_path,
                 file_pattern=settings.default_file, 
                 recursively=False):
        loader = ModuleLoader(names=names, tags=tags)
        classes = list(loader.load(
            base_dir, file_pattern, recursively=recursively))
        module = classes[0]() 
        return module