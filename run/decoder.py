import json
import ipclight
from .request import Request
from .response import Response

class Decoder:
    
    #Public
       
    def decode(self, text_message):
        transport_message = self._make_transport_message(text_message)
        message = self._make_message(transport_message)
        return message

    #Protected
    
    def _make_transport_message(self, text_message):
        return self._transport_decoder.decode(text_message)
    
    #TODO: add error handling
    def _make_message(self, transport_message):
        message_class = self._get_message_class(transport_message)
        content = self._deserialize_content(transport_message.content)
        return message_class(**content)        
   
    def _get_message_class(self, transport_message):
        if isinstance(transport_message, ipclight.Request):
            return Request
        elif isinstance(transport_message, ipclight.Response):
            return Response
        else:
            raise DecodeError('Message type error: '+str(type(transport_message)))
     
    def _deserialize_content(self, serialized_content):
        return json.loads(serialized_content)
        
    #TODO: use cached property
    @property
    def _transport_decoder(self):
        return ipclight.Decoder()

    
class DecodeError(Exception): pass      