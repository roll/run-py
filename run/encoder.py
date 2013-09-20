import ipclight
from .packer import Packer
from .settings import settings

class Encoder:
    
    #Public
    
    #TODO: add error handling/conversion   
    def encode(self, message, protocol=settings.default_protocol):
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