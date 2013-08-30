from abc import ABCMeta
from ipclight import Message, CommonMessage, Request, Response

class Message(Message, metaclass=ABCMeta):
    
    #Public
    
    pass
    
    
class CommonMessage(CommonMessage, Message):
    
    #Public
    
    pass


class Request(CommonMessage, Request): pass
class Response(CommonMessage, Response): pass    

class MessageError(Exception): pass
class MessageTypeError(MessageError): pass 
class MessageParseError(MessageError): pass        