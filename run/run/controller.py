import logging
from ..dispatcher import DispatcherCallbackHandler
from ..task import InitiatedTaskSignal, ProcessedTaskSignal

class RunController:
    
    #Public
    
    def __init__(self, dispatcher, stack=None):
        self._dispatcher = dispatcher
        self._stack = stack
        
    def listen(self):
        self._dispatcher.add_handler(
            self._callback_handler_class(
                self._on_initiated_task, 
                signals=[self._initiated_task_signal_class]))
        self._dispatcher.add_handler(
            self._callback_handler_class(
                self._on_processed_task, 
                signals=[self._processed_task_signal_class]))
         
    #Protected
    
    _callback_handler_class = DispatcherCallbackHandler
    _initiated_task_signal_class = InitiatedTaskSignal
    _processed_task_signal_class = ProcessedTaskSignal
    _logging_module = logging
    
    def _on_initiated_task(self, signal):
        if self._stack != None:
            self._stack.push(signal.attribute)   

    def _on_processed_task(self, signal):
        if self._stack != None:
            message = repr(self._stack)
            self._stack.pop()            
        else:
            message = signal.attribute.meta_qualname            
        logger=self._logging_module.getLogger('processed')
        logger.info(message)    