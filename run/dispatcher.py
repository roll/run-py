import logging
from lib31.python import cachedproperty

class Dispatcher(list):

    #Public

    def push(self, attribute):
        self.append(attribute)
        
    def pop(self):
        attribute = super().pop()
        self._log(self+[attribute])
        return attribute
        
    #Protected
    
    def _log(self, attributes):
        names = []
        previous = attributes[0]
        names.append(previous.meta_name)
        for attribute in attributes[1:]:
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
    

dispatcher = Dispatcher()