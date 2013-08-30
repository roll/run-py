from abc import ABCMeta
from ipclight import Message, CommonMessage

class Message(Message, metaclass=ABCMeta):
    
    #Public
    
    pass
    
    
class CommonMessage(CommonMessage, Message):
    
    #Public
    
    pass
    

class MessageError(Exception): pass
class MessageTypeError(MessageError): pass 
class MessageParseError(MessageError): pass        