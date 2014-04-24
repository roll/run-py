from box.importlib import import_object
from ..settings import settings

class FindModule:

    #Public

    default_filename = settings.default_file    
    default_basedir = settings.default_basedir
    
    def __new__(self, names=[], tags=[], 
                filename=None, basedir=None, recursively=False):
        if not filename:
            filename = self.default_filename
        if not basedir:
            basedir = self.default_basedir
        finder_class = self._get_finder_class() 
        finder = finder_class(names=names, tags=tags)
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
    
    @staticmethod
    def _get_finder_class():
        return import_object('..finder.Finder')