import ipclight

class Decoder:
    
    #Public
       
    def decode(self, data):
        transport_message = self._make_transport_message(data)
        message = self._make_message(transport_message)
        return message

    #Protected
    
    #TODO: implement
    def _make_transport_message(self, data):
        pass
    
    #TODO: implement
    def _make_message(self, transport_message):
        pass
    
    #TODO: use cached property
    @property
    def _transport(self):
        return ipclight.Decoder()