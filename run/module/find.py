class FindModule:

    #Public
    
    def __new__(self, names=None, tags=None, 
                file=None, basedir=None, recursively=False):
        find = self._get_find() 
        module_classes = find(
            names=names,
            tags=tags,
            file=file, 
            basedir=basedir, 
            recursively=recursively)
        for module_class in module_classes:
            module = module_class() 
            return module
        else:
            raise ImportError('Module is not found.')
            
    #Protected
    
    @staticmethod
    def _get_find():
        from ..run import find
        return find