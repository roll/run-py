from abc import ABCMeta
from ipclight import Server, SubprocessServer

class Server(Server, metaclass=ABCMeta):
    
    #Public
    
    pass
    
    
class SubprocessServer(SubprocessServer, Server):
    
    #Public
    
    pass  