import json
import ipclight
from abc import ABCMeta, abstractmethod
from .request import Request
from .response import Response

class Packer(metaclass=ABCMeta):
    
    #Public
    
    @abstractmethod
    def pack(self, message):
        pass #pragma: no cover
    
    
class JSONPacker(Packer):
    
    #Public
    
    #TODO: move default protocol to right place
    def pack(self, message, protocol='run-json-1.0'):
        transport_message_class = self._get_transport_message_class(message)
        
    
    #Protected
   
    def _get_transport_message_class(self, message):
        if isinstance(message, Request):
            return ipclight.Request
        elif isinstance(message, Response):
            return ipclight.Response
        else:
            raise EncodeError('Message type error: '+str(type(message)))
        
    def _serialize_content(self, content):
        return json.dumps(content)