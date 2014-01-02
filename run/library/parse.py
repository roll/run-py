import os
import re
from run import Var, settings

class ParseVar(Var):
    
    #Public
    
    def __init__(self, file_pattern, text_pattern, *,
                 file_pattern_flags=0,                 
                 text_pattern_flags=0,
                 processors=[], 
                 fallback=None,
                 path=settings.default_path):
        self.file_pattern = file_pattern
        self.text_pattern = text_pattern
        self.file_pattern_flags = file_pattern_flags
        self.text_pattern_flags = text_pattern_flags
        self.processors = processors
        self.fallback = fallback
        self.path = path
    
    def retrieve(self):
        try:
            matches = self._search()
            processed = self._process(matches)
            return processed
        except Exception as exception:
            return self._fallback(exception)
    
    #Protected
       
    def _search(self):
        matches = []
        for walkdir, _, filenames in os.walk(self.path):
            for filename in filenames:
                filepath = os.path.join(walkdir, filename)
                if re.search(self.file_pattern, 
                             os.path.relpath(filepath, start=self.path), 
                             self.file_pattern_flags):
                    with open(filepath) as file:
                        matches += re.findall(self.text_pattern, 
                                              file.read(), 
                                              self.text_pattern_flags)
        return matches
        
    def _process(self, value):
        for processor in self.processors:
            value = processor(value)
        return value
    
    def _fallback(self, exception):
        if isinstance(self.fallback, Exception):
            raise self.fallback
        elif callable(self.fallback) and not isinstance(self.fallback, type):
            return self.fallback(exception)
        else:
            return self.fallback