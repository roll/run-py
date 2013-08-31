import ipclight

class Encoder:
    
    #Public
       
    def encode(self, message):
        transport_message = self._make_transport_message(message)
        data = self._make_data(transport_message)
        return data

    #Protected
    
    #TODO: implement
    def _make_transport_message(self, message):
        pass
    
    #TODO: implement
    def _make_data(self):
        pass
    
    #TODO: use cached property
    @property
    def _transport(self):
        return ipclight.Encoder()