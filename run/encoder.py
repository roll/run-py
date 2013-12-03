import ipclight
from packgram.python import cachedproperty
from .packer import Packer
from .settings import settings

class Encoder:
    
    #Public
    
    #TODO: add error handling/convertion   
    def encode(self, message, protocol=settings.default_protocol):
        transport_message = self._transport_packer.pack(message, protocol)
        text_message = self._transport_encoder.encode(transport_message)
        return text_message

    #Protected

    @cachedproperty
    def _transport_packer(self):
        return Packer()
    
    @cachedproperty
    def _transport_encoder(self):
        return ipclight.Encoder()
    
    
class EncodeError(Exception): pass     