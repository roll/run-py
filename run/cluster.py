from .settings import settings

class Cluster:

    #Public

    def __init__(self, names=[], tags=[], 
                 path=settings.default_path,
                 file_pattern=settings.default_file, 
                 recursively=False, 
                 existen=False):
        self._names = names
        self._tags = tags
        self._file_pattern = file_pattern
        self.recursively = recursively
        self.existen = existen