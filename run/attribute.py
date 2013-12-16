import inspect
from abc import ABCMeta, abstractmethod

class Attribute(metaclass=ABCMeta):
    
    #Public
    
    def __new__(cls, *args, **kwargs):
        return AttributeFactory(cls, *args, **kwargs)
#         try:
#             factory = args[0]
#             if not isinstance(factory, AttributeFactory):
#                 raise TypeError()
#         except (KeyError, TypeError):
#             factory = None
#         if factory:
#             return super().__new__(cls, *factory.args, **factory.kwargs)
#         else:    
#             return AttributeFactory(cls, *args, **kwargs)        
       
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
            return AttributeName(
                module=self.module.attrname, 
                attribute=self.module.attributes.find(self))
        except RuntimeError:
            return AttributeName()
 
    @property
    def attrhelp(self):
        return AttributeHelp(signature=self.attrname, 
                             docstring=inspect.getdoc(self))
 
 
class AttributeFactory:
    
    #Public
     
    def __init__(self, cls, *args, **kwargs):
        self._cls = cls
        self._args = args
        self._kwargs = kwargs
        
    @property
    def args(self):
        return self._args

    @property
    def kwargs(self):
        return self._kwargs
        
    def create(self):
        obj = super(Attribute, self._cls).__new__(self._cls)
        self._cls.__init__(obj, *self.args, **self.kwargs)
        return obj
        
        
class AttributeName(str):
    
    #Public
    
    def __new__(cls, module=None, attribute=None):
        name = '.'.join(filter(None, [module, attribute]))
        return super().__new__(cls, name)
    
    def __init__(self, module=None, attribute=None):
        self._module = module or ''
        self._attribute = attribute or ''
    
    @property    
    def module(self):
        return self._module
    
    @property
    def attribute(self):
        return self._attribute    
    

class AttributeHelp(str):
    
    #Public
    
    def __new__(cls, signature=None, docstring=None):
        hlp = '\n'.join(filter(None, [signature, docstring]))
        return super().__new__(cls, hlp)
    
    def __init__(self, signature=None, docstring=None):
        self._signature = signature or ''
        self._docstring = docstring or ''
    
    @property    
    def signature(self):
        return self._signature
    
    @property
    def docstring(self):
        return self._docstring
    
    
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