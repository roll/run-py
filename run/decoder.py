import ipclight

class Decoder:
    
    #Public
       
    def decode(self, string):
        transport_message = self._make_transport_message(string)
        message = self._make_message(transport_message)
        return message

    #Protected
    
    #TODO: implement
    def _make_transport_message(self, string):
        return self._transport.decode(string)
    
    #TODO: implement
    def _make_message(self, transport_message):
        pass
    
    #TODO: use cached property
    @property
    def _transport(self):
        return ipclight.Decoder()