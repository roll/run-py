import ipclight

class Encoder:
    
    #Public
       
    pass

    #Protected
    
    #TODO: use cached property
    @property
    def transport(self):
        return ipclight.Encoder()