import inspect
from abc import ABCMeta
from .attribute import Attribute, AttributeProxy
from .module import Module
from .settings import settings
from .task import Task, MethodTask
from .var import PropertyVar, ValueVar

class RunMeta(ABCMeta):
     
    #Public
     
    def __new__(cls, name, bases, dct):
        mrodict = {}
        for base in reversed(cls.__get_mro(bases)):
            mrodict.update(base.__dict__)
        mrodict.update(dct)
        for key, attr in mrodict.items():
            if (not key.startswith('_') and
                not key in ['attributes', 'module'] and
                not isinstance(attr, type)):
                if isinstance(attr, Attribute):
                    attr = attr
                elif isinstance(attr, AttributeProxy):
                    attr = attr()
                elif callable(attr):
                    attr = MethodTask(attr)()
                elif inspect.isdatadescriptor(attr):
                    attr = PropertyVar(attr)()
                else:
                    attr = ValueVar(attr)()
                dct[key] = attr
        return super().__new__(cls, name, bases, dct)
     
    #Private
    
    #TODO: implement
    @classmethod
    def __get_mro(cls, bases):
        return bases[0].mro()
    

class Run(Module, metaclass=RunMeta):
    
    #Public
    
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)
    
    def __call__(self, attribute, *args, **kwargs):
        if not attribute:
            attribute = settings.default_attribute
        attribute = getattr(self, attribute)
        if callable(attribute):
            result = attribute(*args, **kwargs)
            return result
        else:
            return attribute
    
    @property
    def runname(self):
        return ''
    
    @property
    def runtags(self):
        return []

    def list(self):
        "List attributes"
        for attribute in self.attributes:
            print(attribute)

    def help(self, attribute):
        "Print attribute help"
        if attribute in self.attributes:
            print(self.attributes[attribute].attrhelp)
        else:
            raise RuntimeError('No attribute "{0}"'.format(attribute))
      
    default = Task(
        require=['list'],
    )        