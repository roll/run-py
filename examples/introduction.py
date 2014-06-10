from run import Module, InputVar, require, trigger

class Module(Module):
    
    #Tasks
    
    def ready(self):
        print('We\'re ready to say', self.greeting, 'to person.')
    
    @require('ready')
    @trigger('done')
    def greet(self, person='World', times=3):
        """Greet the given person."""
        print(self.greeting, person, str(times), 'times!')
        
    def done(self):
        print('We\'re done.')
        
    #Vars
    
    greeting = InputVar(
        prompt='Type your greeting',
        default='Hello',
    )