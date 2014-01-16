from run import Module
from box.findtools import find_files, find_strings, find_objects

class FindModule(Module):
    
    #Public

    def find_files(self, *args, **kwargs):
        return self._find_files_function(*args, **kwargs)
    
    def find_strings(self, *args, **kwargs):
        return self._find_strings_function(*args, **kwargs)
    
    def find_objects(self, *args, **kwargs):
        return self._find_objects_function(*args, **kwargs)
    
    #Protected
    
    _find_files_function = staticmethod(find_files)
    _find_strings_function = staticmethod(find_strings)
    _find_objects_function = staticmethod(find_objects)