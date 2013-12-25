from abc import ABCMeta, abstractmethod
from ..dependent import DependentAttribute

class Var(DependentAttribute, metaclass=ABCMeta):
    
    #Public

    def __get__(self, module, module_class=None):
        self._resolve_requirements()
        #TODO: add error handling   
        result = self.retrieve()
        self._process_triggers()
        #TODO: reimplement!
        print('Retrieved: '+self.meta_name)
        #print('Retrieved '+str(self))             
        return result
 
    @abstractmethod
    def retrieve(self):
        pass #pragma: no cover
    
    
    
        