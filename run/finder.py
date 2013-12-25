import os
import re
import sys
import inspect
import importlib

class Finder:

    #Public

    @classmethod
    def find(cls, base_dir, file_pattern, **object_filters):
        files = cls._find_files(base_dir, pattern=file_pattern)
        modules = cls._import_modules(files)
        objects = cls._find_classes(modules)
        filtered_objects = cls._filter_objects(objects, **object_filters)
        return filtered_objects
            
    #Protected
    
    @staticmethod
    def _find_files(base_dir, file_pattern=''):
        files = []
        for dir_path, _, file_names in os.walk(base_dir):
            for file_name in file_names:
                if re.match(file_pattern, file_name):
                    files.append(os.path.join(dir_path, file_name))
        return files
    
    @staticmethod    
    def _import_modules(files):
        modules = []
        for file in files:
            dir_name, file_name = os.path.split(os.path.abspath(file))
            module_name = re.sub('\.pyc?', '', file_name)
            sys.path.insert(0, dir_name)
            module = importlib.import_module(module_name)
            modules.append(module)
        return modules
        
    @staticmethod        
    def _get_objects(modules):
        objects = []
        for module in modules:
            for name in dir(module):
                attr = getattr(module, name)
                if inspect.getmodule(attr) == module:
                    objects.append(attr)
        return objects
    
    @staticmethod    
    def _filter_objects(objects, **object_filters):
        return objects