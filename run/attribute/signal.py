from ..signal import Signal

class AttributeSignal(Signal):

    #Public

    def __init__(self, attribute):
        self._attribute = attribute
    
    @property    
    def attribute(self):
        return self._attribute