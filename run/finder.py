import os
import re
import sys
import inspect
import importlib
from .module import Module
from .settings import settings

class Finder:

    #Public

    def find(self, path, **constraints):
        files = self._find_files(path, name=settings.default_runfile)
        modules = self._find_classes(files, parent=Module)
        filtered_modules = self._filter_classes(modules, constraints)
        return filtered_modules
            
    #Protected        
    
    def _find_files(self, path, name):
        """Find files recursively in path
           where filename == name"""      
        files = []
        for root, _, files in os.walk(path):
            for file in files:
                if file == name:
                    files.append(os.path.join(root, file))
        return files
        
    def _find_classes(self, files, bases=[]):
        """Find and import classes of files
           where issubclass(class, tuple(bases))"""
        classes = []
        for file in files:
            dirname, filename = os.path.split(os.path.abspath(file))
            modulename = re.sub('\.pyc?', '', filename)
            sys.path.insert(dirname)
            module = importlib.import_module(modulename)
            for name in dir(module):
                attr = getattr(module, name)
                if (isinstance(attr, type) and
                    inspect.getmodule(attr) == module and
                    (not bases or issubclass(attr, tuple(bases))) and
                    not inspect.isabstract(attr)):
                    classes.append[attr]
        return classes
    
    def _filter_classes(self, classes, constraints):
        pass