from .attributes import ModuleAttributes
from .builder import ModuleBuilder
from .module import ModuleMeta, Module

#Remove modules
from lib31 import python
python.remove_modules(locals())