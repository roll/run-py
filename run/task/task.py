from ..dependent import DependentAttribute

class Task(DependentAttribute):
    
    #Public
    
    def __get__(self, module, module_class=None):
        return self
    
    def __call__(self, *args, **kwargs):
        self.meta_logger.debug('requested')
        self._resolve_requirements()
        self.meta_logger.debug('requirements resolved')
        result = self.complete(*args, **kwargs)
        self._process_triggers()
        self.meta_logger.debug('triggers processed')
        self.meta_logger.info('completed')
        return result
    
    def complete(self, *args, **kwargs):
        pass