import logging
from contextlib import contextmanager
from lib31.python import cachedproperty

class Dispatcher:

    #Public
    
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
        

dispatcher = Dispatcher()