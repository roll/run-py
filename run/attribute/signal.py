from ..dispatcher import DispatcherSignal

class AttributeSignal(DispatcherSignal):

    #Public

    def __init__(self, attribute):
        self._attribute = attribute
    
    @property    
    def attribute(self):
        return self._attribute