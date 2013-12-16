from abc import ABCMeta, abstractmethod
from .unit import Unit, UnitName, UnitHelp

class Attribute(Unit, metaclass=ABCMeta):
    
    #Public
       
    @abstractmethod
    def __get__(self, namespace, namespace_class):
        pass #pragma: no cover
    
    def __set__(self, namespace, value):
        raise RuntimeError('Can\'t set attribute')

    #TODO: use NullNamespace?
    @property
    def namespace(self):
        try:
            return self.__namespace
        except AttributeError:
            raise RuntimeError(
                'Attribute "{0}" is not attached to any namespace'.
                format(self))
    
    @namespace.setter
    def namespace(self, namespace):
        try: 
            if self.__namespace != namespace:
                print(self.unitname)
                print(namespace)
                raise RuntimeError(
                    'Attribute "{0}" is already attached to namespace "{1}"'.
                    format(self, self.__namespace))
        except AttributeError:
            self.__namespace = namespace
    
    @property
    def unitname(self):
        try:
            return UnitName(namespace=self.namespace.unitname, 
                            attribute=self.namespace.attributes.find(self))
        except RuntimeError:
            return super().unitname
 
    @property
    def unithelp(self):
        return UnitHelp(signature=self.unitname, 
                        docstring=super().unithelp.docstring)
    
    
class AssociatedAttribute(Attribute):
    
    #Public
    
    def __init__(self, *args, **kwargs):
        self.__require = kwargs.pop('require', [])
        super().__init__(*args, **kwargs)
    
    #TODO: make it happened just one time
    def resolve(self):
        for task_name in self.__require:
            task = getattr(self.namespace, task_name)
            task()    