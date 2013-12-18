import inspect
from abc import ABCMeta, abstractmethod

class Attribute(metaclass=ABCMeta):
    
    #Public
    
    def __new__(cls, *args, **kwargs):
        return AttributeBuilder(cls, *args, **kwargs)
    
    def __init__(self, *args, **kwargs):
        self.__signature = kwargs.pop('signature', None)
        self.__docstring = kwargs.pop('docstring', None)
        self.__module = None
    
    @abstractmethod
    def __get__(self, module, module_class):
        pass #pragma: no cover
    
    def __set__(self, module, value):
        raise RuntimeError('Can\'t set attribute')

    @property
    def module(self):
        return self.__module
    
    @module.setter
    def module(self, module):
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
        return AttributeMetadata(
            self, self.__signature, self.__docstring)
        
  
class AttributeBuilder:
    
    #Public
    
    def __init__(self, cls, *args, **kwargs):
        self._class = cls
        self._args = args
        self._kwargs = kwargs
        
    def __call__(self):
        obj = self._make_object()
        self._sys_init_object(obj)
        return obj
    
    #Protected

    _sys_init_classes = [Attribute]
    _sys_kwarg_keys = ['signature', 'docstring']
           
    def _sys_init_object(self, obj):
        sys_kwargs = self._make_sys_kwargs()
        for cls in self._sys_init_classes:
            cls.__init__(obj, **sys_kwargs)
    
    def _make_object(self):
        user_kwargs = self._make_user_kwargs()
        obj = object.__new__(self._class)
        obj.__init__(*self._args, **user_kwargs)
        return obj

    def _make_sys_kwargs(self):
        kwargs = {}
        for key, value in self._kwargs.items():
            if key in self._sys_kwarg_keys:
                kwargs[key] = value
        return kwargs

    def _make_user_kwargs(self):
        kwargs = {}
        for key, value in self._kwargs.items():
            if key not in self._sys_kwarg_keys:
                kwargs[key] = value
        return kwargs


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

    def __new__(cls, *args, **kwargs):
        return DependentAttributeBuilder(cls, *args, **kwargs)
    
    def __init__(self, *args, **kwargs):
        self.__require = kwargs.pop('require', [])
    
    #TODO: make it happened just one time
    def resolve(self):
        for task_name in self.__require:
            task = getattr(self.module, task_name)
            task()


class DependentAttributeBuilder(AttributeBuilder):
    
    #Protected

    @property
    def _sys_init_classes(self):
        return super()._sys_init_classes+[DependentAttribute]

    @property
    def _sys_kwarg_keys(self):
        return super()._sys_kwarg_keys+['require']
