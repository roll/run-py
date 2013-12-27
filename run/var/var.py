from abc import ABCMeta, abstractmethod
from ..dependent import DependentAttribute
from ..dispatcher import dispatcher

class Var(DependentAttribute, metaclass=ABCMeta):
    
    #Public

    def __get__(self, module, module_class=None):
        dispatcher.push(self)
        #self.meta_logger.debug('requested')
        self._resolve_requirements()
        #self.meta_logger.debug('requirements resolved')
        result = self.retrieve()
        self._process_triggers()
        #self.meta_logger.debug('triggers processed')
        #self.meta_logger.info('retrieved')
        dispatcher.pop()        
        return result
 
    @abstractmethod
    def retrieve(self):
        pass #pragma: no cover
    
    
    
        