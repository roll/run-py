from runclasses.python_package import PythonPackageRunclass
from package import package
    
class Runclass(PythonPackageRunclass):
        
    #Public
    
    def __init__(self):
        self._package = package