import inspect
from abc import ABCMeta, abstractmethod

class Attribute(metaclass=ABCMeta):
    
    #Public
       
    @abstractmethod
    def __get__(self, module, module_class):
        pass #pragma: no cover
    
    def __set__(self, module, value):
        raise RuntimeError('Can\'t set attribute')

    #TODO: use NullModule?
    @property
    def module(self):
        try:
            return self.__module
        except AttributeError:
            raise RuntimeError(
                'Attribute "{0}" is not attached to any module'.
                format(self))
    
    @module.setter
    def module(self, module):
        try: 
            if self.__module != module:
                raise RuntimeError(
                    'Attribute "{0}" is already attached to module "{1}"'.
                    format(self, self.__module))
        except AttributeError:
            self.__module = module
    
    @property
    def attrname(self):
        try:
            return AttributeName(module=self.module.unitname, 
                                 attribute=self.module.attributes.find(self))
        except RuntimeError:
            return super().unitname
 
    @property
    def attrhelp(self):
        return AttributeHelp(signature=self.unitname, 
                             docstring=inspect.getdoc(self))
        
        
class DependentAttribute(Attribute):
    
    #Public
    
    def __init__(self, *args, **kwargs):
        self.__require = kwargs.pop('require', [])
        super().__init__(*args, **kwargs)
    
    #TODO: make it happened just one time
    def resolve(self):
        for task_name in self.__require:
            task = getattr(self.module, task_name)
            task() 
            
                    
class AttributeName(str):
    
    #Public
    
    def __new__(cls, module='', attribute=''):
        name = '.'.join(filter(None, [module, attribute]))
        return super().__new__(cls, name)
    
    def __init__(self, module='', attribute=''):
        self._module = module
        self._attribute = attribute
    
    @property    
    def module(self):
        return self._module
    
    @property
    def attribute(self):
        return self._attribute    
    

class AttributeHelp(str):
    
    #Public
    
    def __new__(cls, signature='', docstring=''):
        hlp = '\n'.join(filter(None, [signature, docstring]))
        return super().__new__(cls, hlp)
    
    def __init__(self, signature='', docstring=''):
        self._signature = signature
        self._docstring = docstring
    
    @property    
    def signature(self):
        return self._signature
    
    @property
    def docstring(self):
        return self._docstring