from run import Module
from box.findtools import find_files, find_strings, find_objects

class FindModule(Module):
    
    BREAK_BEFORE = find_files.BREAK_BEFORE
    BREAK_AFTER = find_files.BREAK_AFTER
    
    #Public

    def find_files(self, *args, **kwargs):
        return find_files(*args, **kwargs)
    
    def find_strings(self, *args, **kwargs):
        return find_strings(*args, **kwargs)
    
    def find_objects(self, *args, **kwargs):
        return find_objects(*args, **kwargs)