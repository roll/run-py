import json
import ipclight
from .request import Request
from .response import Response

class Unpacker:
    
    #Public
    
    def unpack(self, transport_message):
        message_class = self._get_message_class(transport_message)
        message_content = self._get_message_content(transport_message)
        return message_class(**message_content)
    
    #Protected
    def _get_message_class(self, transport_message):
        if isinstance(transport_message, ipclight.Request):
            return Request
        elif isinstance(transport_message, ipclight.Response):
            return Response
        else:
            raise UnpackError('Message type error: '+str(type(transport_message)))
   
    def _get_message_content(self, transport_message):
        if transport_message.protocol == 'run-json-1.0':
            return json.loads(transport_message.content)
        else:
            raise UnpackError('Unsupported protocol: '+transport_message.protocol)               
    
    
class UnpackError(Exception): pass       