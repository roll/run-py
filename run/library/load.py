from run import Loader, settings

class LoadModule:

    #Public

    def __new__(self, names=[], tags=[], 
                basedir=None, file_pattern=None, recursively=False):
        if not basedir:
            basedir = self._default_basedir
        if not file_pattern:
            file_pattern = self._default_file_pattern
        loader = self._loader_class(names=names, tags=tags)
        for module_class in loader.load(basedir, file_pattern, recursively):
            module = module_class() 
            return module
        else:
            raise ImportError(
                'No modules found with names "{names}", tags "{tags}", '
                'basedir "{basedir}", file_pattern "{file_pattern}" and '
                'recursively flag in "{recursively}"'.
                format(names=names, tags=tags, basedir=basedir, 
                       file_pattern=file_pattern, 
                       recursively=recursively))
            
    #Protected
    
    _loader_class = Loader
    _default_basedir = settings.default_basedir
    _default_file_pattern = settings.default_file