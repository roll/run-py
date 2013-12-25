class ModuleLoaderFilter:

    #Public

    def __init__(self, filt):
        self._filter = filt
        
    def filter(self, module_class):
        return True