import logging
from ..dispatcher import DispatcherCallbackHandler
from ..task import InitiatedTaskSignal, SuccessedTaskSignal, FailedTaskSignal

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
                self._on_successed_task, 
                signals=[self._successed_task_signal_class]))
        self._dispatcher.add_handler(
            self._callback_handler_class(
                self._on_failed_task, 
                signals=[self._failed_task_signal_class]))        
         
    #Protected
    
    _callback_handler_class = DispatcherCallbackHandler
    _initiated_task_signal_class = InitiatedTaskSignal
    _successed_task_signal_class = SuccessedTaskSignal
    _failed_task_signal_class = FailedTaskSignal
    _logging_module = logging
    
    def _on_initiated_task(self, signal):
        if self._stack != None:
            self._stack.push(signal.attribute)   

    def _on_successed_task(self, signal):
        if self._stack != None:
            message = repr(self._stack)
            self._stack.pop()            
        else:
            message = signal.attribute.meta_qualname            
        logger=self._logging_module.getLogger('successed')
        logger.info(message)
        
    def _on_failed_task(self, signal):
        if self._stack != None:
            message = repr(self._stack)
        else:
            message = signal.attribute.meta_qualname            
        logger=self._logging_module.getLogger('failed')
        logger.info(message)         