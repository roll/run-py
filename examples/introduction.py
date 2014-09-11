from run import Module, PromptVar, require, trigger


class IntroductionModule(Module):

    # Tasks

    def ready(self):
        print('We are ready to say', self.greeting, 'to person.')

    @require('ready')
    @trigger('done')
    def greet(self, person='World', times=3):
        """Greet the given person."""
        print(self.greeting, person, str(times), 'times!')

    def done(self):
        print('We are done.')

    # Vars

    greeting = PromptVar(
        prompt='Type your greeting',
        default='Hello',
    )
