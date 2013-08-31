import ipclight

class Encoder:
    
    #Public
       
    def encode(self, message):
        transport_message = self._make_transport_message(message)
        text_message = self._make_text_message(transport_message)
        return text_message

    #Protected
    
    #TODO: implement
    def _make_transport_message(self, message):
        pass
    
    def _make_text_message(self, transport_message):
        return self._transport_encoder.encode(transport_message)
    
    #TODO: use cached property
    @property
    def _transport_encoder(self):
        return ipclight.Encoder()