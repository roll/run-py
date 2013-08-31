import ipclight

class Decoder:
    
    #Public
       
    pass

    #Protected
    
    #TODO: use cached property
    @property
    def transport(self):
        return ipclight.Decoder()