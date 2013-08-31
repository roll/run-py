import ipclight

class Encoder:
    
    #Public
       
    pass

    #Protected
    
    def _make_transport_message(self):
        pass
    
    def _make_data(self):
        pass
    
    #TODO: use cached property
    @property
    def _transport(self):
        return ipclight.Encoder()