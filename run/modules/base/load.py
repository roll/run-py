from run import Loader, settings

class LoadModule:

    #Public

    def __new__(self, names=[], tags=[],
                 path=settings.default_path,
                 file_pattern=settings.default_file, 
                 recursively=False):
        loader = Loader(names=names, tags=tags)
        for module_class in loader.load(path, file_pattern, recursively):
            module = module_class() 
            return module
        else:
            raise ImportError(
                'No modules finded with '
                'names "{0}", tags "{1}", path "{2}", '
                'file_pattern "{3}" and recursively flag in "{4}"'.
                format(names, tags, path, file_pattern, recursively))