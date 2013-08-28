class Run:
    
    #Public
    
    #TODO: add accidental redefinition proof 
    def respond(self, request=None):
        if request:
            return self._internal_respond(request)
        else:
            self._external_respond()
    
    #Protected
    
    def _internal_respond(self, request):
        pass
    
    def _external_respond(self):
        pass