import ipclight

class Decoder:
    
    #Public
       
    pass

    #Protected
    
    #TODO: use cached property
    @property
    def _transport(self):
        return ipclight.Decoder()