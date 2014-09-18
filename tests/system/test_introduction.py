from tests.system.test_demo import DemoTest


class IntroductionTest(DemoTest):

    # Actions

    __test__ = True

    # Helpers

    @property
    def filename(self):
        return 'introduction.py'

    # Tests

    def test_greet(self):
        result = self.execute('greet', messages=['Hi'])
        self.assertEqual(
            result,
            'Type your greeting ([Hello]/*): '
            'We are ready to say Hi to person.\n'
            'Hi World 3 times!\n'
            'We are done.\n')
