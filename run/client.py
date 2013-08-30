from abc import ABCMeta
from ipclight import Client, SubprocessClient

class Client(Client, metaclass=ABCMeta):
    
    #Public
    
    pass
    
    
class SubprocessClient(SubprocessClient, Client):
    
    #Public
    
    pass  