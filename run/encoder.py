import ipclight

class Encoder:
    
    #Public
       
    def encode(self, message):
        transport_message = self._make_transport_message(message)
        string = self._make_string(transport_message)
        return string

    #Protected
    
    #TODO: implement
    def _make_transport_message(self, message):
        pass
    
    #TODO: implement
    def _make_string(self, transport_message):
        pass
    
    #TODO: use cached property
    @property
    def _transport(self):
        return ipclight.Encoder()