from run import Loader, settings

class LoadModule:

    #Public

    def __new__(self, names=[], tags=[], path=None, 
                file_pattern=None, recursively=False):
        if not path:
            path = self._default_path
        if not file_pattern:
            file_pattern = self._default_file_pattern
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
    
    _default_path = settings.default_path
    _default_file_pattern = settings.default_file
    _loader_class = Loader