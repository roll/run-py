import json
import ipclight
from .request import Request
from .response import Response

class Packer:
    
    #Public
    
    #TODO: move default protocol to the right place
    def pack(self, message, protocol='run-json-1.0'):
        transport_message_class = self._get_transport_message_class(message)
        transport_message_content = self._get_transport_message_content(message, protocol)
        return transport_message_class(protocol, transport_message_content)
    
    #Protected
   
    def _get_transport_message_class(self, message):
        if isinstance(message, Request):
            return ipclight.Request
        elif isinstance(message, Response):
            return ipclight.Response
        else:
            raise PackError('Message type error: '+str(type(message)))
        
    def _get_transport_message_content(self, message, protocol):
        if protocol == 'run-json-1.0':
            return json.dumps(message.content)
        else:
            raise PackError('Unsupported protocol: '+protocol)
    

class PackError(Exception): pass     