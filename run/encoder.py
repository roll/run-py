import ipclight
from .packer import Packer

class Encoder:
    
    #Public
       
    #TODO: move default protocol to the right place       
    def encode(self, message, protocol='run-json-1.0'):
        transport_message = self._transport_packer.pack(message, protocol)
        text_message = self._transport_packer.encode(transport_message)
        return text_message

    #Protected

    #TODO: use cachedproperty
    @property
    def _transport_packer(self):
        return Packer()
    
    #TODO: use cachedproperty
    @property
    def _transport_encoder(self):
        return ipclight.Encoder()
    
    
class EncodeError(Exception): pass     