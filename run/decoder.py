import ipclight

class Decoder:
    
    #Public
       
    def decode(self, data):
        pass

    #Protected
    
    def _make_transport_message(self):
        pass
    
    def _make_message(self):
        pass
    
    #TODO: use cached property
    @property
    def _transport(self):
        return ipclight.Decoder()