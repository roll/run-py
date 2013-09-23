from lib31.console import Command

class Command(Command):
    
    #Public
      
    @property
    def _request(self):
        #TODO: reimplement
        method = self._command.method
        arguments, options = self._parse_parameters(self._command.parameters)
        request = Request(method, arguments, options)
        return request
    
    #TODO: implement
    def _parse_parameters(self):
        pass    