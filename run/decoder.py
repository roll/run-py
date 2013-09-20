import ipclight
from .unpacker import Unpacker

class Decoder:
    
    #Public
       
    #TODO: add error handling/conversion       
    def decode(self, text_message):
        transport_message = self._transport_decoder.decode(text_message)
        message = self._transport_unpacker.unpack(transport_message)
        return message

    #Protected

    #TODO: use cached property
    @property
    def _transport_decoder(self):
        return ipclight.Decoder()
    
    #TODO: use cached property
    @property
    def _transport_unpacker(self):
        return Unpacker()    

    
class DecodeError(Exception): pass      