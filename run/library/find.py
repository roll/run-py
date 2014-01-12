from run import Finder, settings

class FindModule:

    #Public

    def __new__(self, names=[], tags=[], 
                filename=None, basedir=None, recursively=False):
        if not basedir:
            basedir = self._default_basedir
        if not filename:
            filename = self._default_filename
        finder = self._finder_class(names=names, tags=tags)
        for module_class in finder.find(filename, basedir, recursively):
            module = module_class() 
            return module
        else:
            raise ImportError(
                'No modules found with names "{names}", tags "{tags}", '
                'basedir "{basedir}", filename "{filename}" and '
                'recursively flag in "{recursively}"'.
                format(names=names, tags=tags, basedir=basedir, 
                       filename=filename, 
                       recursively=recursively))
            
    #Protected
    
    _finder_class = Finder
    _default_basedir = settings.default_basedir
    _default_file_pattern = settings.default_file