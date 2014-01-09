import logging
from box.python import cachedproperty
from .handler import CallbackHandler
from .stack import Stack
from .task import InitiatedTaskSignal, CompletedTaskSignal
from .var import InitiatedVarSignal, RetrievedVarSignal

class Controller:
    
    #Public
    
    def __init__(self, dispatcher, stackless=False):
        self._dispatcher = dispatcher
        self._stackless = stackless
        
    def listen(self):
        self._dispatcher.add_handler(
            self._callback_handler_class(
                self._on_initiated_attribute, 
                signals=[self._initiated_task_signal_class, 
                         self._initiated_var_signal_class]))
        self._dispatcher.add_handler(
            self._callback_handler_class(
                self._on_executed_attribute, 
                signals=[self._completed_task_signal_class, 
                         self._retrieved_var_signal_class]))
         
    #Protected
    
    _callback_handler_class = CallbackHandler
    _initiated_task_signal_class = InitiatedTaskSignal
    _initiated_var_signal_class = InitiatedVarSignal
    _completed_task_signal_class = CompletedTaskSignal
    _retrieved_var_signal_class = RetrievedVarSignal
    _logging_module = logging
    _stack_class = Stack
    
    def _on_initiated_attribute(self, signal):
        if not self._stackless:
            self._stack.push(signal.attribute)   

    def _on_executed_attribute(self, signal):
        if not self._stackless:
            message = str(self._stack)
            self._stack.pop()            
        else:
            message = signal.attribute.meta_qualname            
        logger=self._logging_module.getLogger('executed')
        logger.info(message) 
        
    @cachedproperty
    def _stack(self):
        return self._stack_class()       