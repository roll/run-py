from run import Loader, settings

class LoadModule:

    #Public

    def __new__(self, names=[], tags=[],
                 path=settings.default_path,
                 file_pattern=settings.default_file, 
                 recursively=False):
        loader = self._loader_class(names=names, tags=tags)
        for module_class in loader.load(path, file_pattern, recursively):
            module = module_class() 
            return module
        else:
            raise ImportError(
                'No modules found with names "{names}", tags "{tags}", '
                'path "{path}", file_pattern "{file_pattern}" and '
                'recursively flag in "{recursively}"'.
                format(names=names, tags=tags, path=path, 
                       file_pattern=file_pattern, 
                       recursively=recursively))
            
    #Protected
    
    _loader_class = Loader