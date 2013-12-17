import inspect
from abc import ABCMeta, abstractmethod

class Attribute(metaclass=ABCMeta):
    
    #Public
    
    def __new__(cls, *args, **kwargs):
        return AttributeBuilder(cls, *args, **kwargs)
    
    def __init__(self, *args, **kwargs):
        self.__signature = kwargs.pop('signature', None)
        self.__docstring = kwargs.pop('docstring', None)
    
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
                'Attribute "{0}" is not bound to any module'.
                format(self))
    
    @module.setter
    def module(self, module):
        try: 
            if self.__module != module:
                raise RuntimeError(
                    'Attribute "{0}" is already bound to module "{1}"'.
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
    
    def metadata(self):
        return AttributeMetadata(self)
        
  
class AttributeBuilder:
    
    #Public
    
    def __init__(self, cls, *args, **kwargs):
        self._signature = kwargs.pop('signature', None)
        self._docstring = kwargs.pop('docstring', None)
        self._class = cls
        self._args = args
        self._kwargs = kwargs
        
    def __call__(self):
        obj = self._make_object()
        self._extend_object(obj)
        return obj
    
    #Protected
    
    def _extend_object(self, obj):
        Attribute.__init__(obj, signature=self._signature,
                           docstring=self._docstring)
    
    def _make_object(self):
        obj = object.__new__(self._class)
        obj.__init__(*self._args, **self._kwargs)
        return obj


class AttributeMetadata:
    
    #Public
    
    def __init__(self, attribute, signature=None, docstring=None):
        self._attribute = attribute
        self._signature = signature
        self._docstring = docstring

    @property
    def name(self):
        pass
    
    @property
    def module_name(self):
        pass    
    
    @property
    def attribute_name(self):
        pass 
    
    @property
    def signature(self):
        pass    
    
    @property
    def docstring(self):
        pass    
  
        
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
        super().__init__(*args, **kwargs)
        self.__require = kwargs.pop('require', [])
    
    #TODO: make it happened just one time
    def resolve(self):
        for task_name in self.__require:
            task = getattr(self.module, task_name)
            task()    