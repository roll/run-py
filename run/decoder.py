import ipclight

class Decoder:
    
    #Public
       
    def decode(self, text_message):
        transport_message = self._make_transport_message(text_message)
        message = self._make_message(transport_message)
        return message

    #Protected
    
    def _make_transport_message(self, text_message):
        return self._transport.decode(text_message)
    
    #TODO: implement
    def _make_message(self, transport_message):
        pass
    
    #TODO: use cached property
    @property
    def _transport(self):
        return ipclight.Decoder()