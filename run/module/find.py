from box.dependency import inject
from box.functools import Function, cachedproperty

class FindModule(Function):

    #Public
    
    def __init__(self, names=None, tags=None, *,
                file=None, basedir=None, recursively=False):
        self._names = names
        self._tags = tags
        self._file = file
        self._basedir = basedir
        self._recursively = recursively
        
    def __call__(self):
        try:
            return self._module
        except self._not_found:
            raise ImportError('Module is not found.') from None
        
    #Protected
    
    _find_files = inject('find_files', module='run.cluster')
    _find_modules = inject('find_modules', module='run.cluster')
    _not_found = inject('NotFound', module='run.cluster')
    
    @cachedproperty
    def module(self):
        module = self._module_class()
        return module
    
    @cachedproperty
    def module_class(self):
        module_class = self._find_modules(
            names=self._names,
            tags=self._tags,
            files=self._files,                
            getfirst=True)
        return module_class
    
    @cachedproperty
    def files(self):
        files = self._find_files(
            file=self._file, 
            basedir=self._basedir, 
            recursively=self._recursively,
            join=True)
        return files