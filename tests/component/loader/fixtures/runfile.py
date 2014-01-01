from abc import abstractmethod
from run import Module

class Module1(Module):
    
    #Public
    
    meta_name = 'name1'
    meta_tags = ['tag1']


#Should be ignored by loader

class AbstractModule(Module):
    
    #Public
    
    @abstractmethod
    def method(self):
        pass #pragma: no cover
 
    
class Class: pass
def function(): pass