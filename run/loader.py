from lib31.python import ObjectLoader
    
class ModuleLoader(ObjectLoader):
    
    #Public
    
    def load(self, base_dir, file_pattern):
        objects = super().load(base_dir, file_pattern)
        return objects