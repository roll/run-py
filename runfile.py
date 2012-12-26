from package import package

try:
    from runclasses.package import PackageRunclass
    base = PackageRunclass
except ImportError:
    base = object
    
class Runclass(base):
        
    #Protected
        
    _package = package