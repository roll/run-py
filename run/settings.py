from lib31.package import Settings

class Settings(Settings):
    
    #Public
    
    default_protocol = 'run-json-1.0' 
    
    @property
    def command_schema(self):
        return {
            'prog': 'run',
            'add_help': False,                     
            'arguments': [
                {
                 'name': 'method',
                },
                {
                 'name': 'arguments',
                 'nargs':'*',
                 'default': [],
                },             
                {
                 'dest': 'server',
                 'flags': ['-s', '--server'], #TODO: make no required
                 'required': True,
                },   
                {
                 'dest': 'protocol', 
                 'flags': ['-p', '--protocol'],
                 'default': self.default_protocol,               
                },                                     
            ],        
        }
   
    
settings = Settings()