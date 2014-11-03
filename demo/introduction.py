from run import Module, require, trigger


class IntroductionModule(Module):

    # Tasks

    def ready(self):
        print('We are ready.')

    @require('ready')
    @trigger('done')
    def hello(self, person='World', times=3):
        """Say hello to the given person."""
        print('Hello', person, str(times), 'times!')

    def done(self):
        print('We are done.')
