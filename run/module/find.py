class FindModule:

    #Public
    
    def __new__(self, names=None, tags=None, *,
                file=None, basedir=None, recursively=False, **find_params):
        find = self._get_find() 
        module_classes = find(
            names=names,
            tags=tags,
            file=file, 
            basedir=basedir, 
            recursively=recursively,
            **find_params)
        for module_class in module_classes:
            module = module_class() 
            return module
        else:
            raise ImportError('Module is not found.')
            
    #Protected
    
    @staticmethod
    def _get_find():
        from ..system import find
        return find