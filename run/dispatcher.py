import logging
from contextlib import contextmanager
from lib31.python import cachedproperty

class Dispatcher:

    #Public
    
    def __init__(self):
        self._handlers = []
        self._signals = []
    
    def add_handler(self, callback, bases=[]):
        handler = DispatcherHandler(callback, bases)
        self._handlers.append(handler)
    
    def add_signal(self, signal):
        self._signals.append(signal)
        for handler in self._handlers:
            handler.handle(signal)            
    
    @contextmanager
    def register(self, attribute):
        self._stack.append(attribute)
        yield
        self._log()
        self._stack.pop()
        
    #Protected
    
    def _log(self):
        names = []
        previous = self._stack[0]
        names.append(previous.meta_name)
        for attribute in self._stack[1:]:
            current = attribute
            if current.meta_module == previous.meta_module:
                names.append(current.meta_attribute_name)
            else:
                names.append(current.meta_name) 
            previous = current
        self._logger.info('[+] '+'/'.join(names))
  
    @cachedproperty
    def _logger(self):
        formatter = logging.Formatter('%(message)s')
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        logger = logging.getLogger('stack')
        logger.addHandler(handler)
        logger.propagate = False
        return logger

    @cachedproperty    
    def _stack(self):
        return []
        
        
class DispatcherHandler:
    
    #Public
    
    def __init__(self, callback, bases=[]):
        self._callback = callback
        self._bases = bases
        
    def handle(self, signal):
        if isinstance(signal, tuple(self._bases)):
            self._callback()    
    

class DispatcherSignal:
    
    #Public
    
    pass


dispatcher = Dispatcher()