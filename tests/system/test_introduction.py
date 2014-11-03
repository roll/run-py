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
        result = self.execute('hello', messages=['Hi'])
        self.assertEqual(
            result,
            'We are ready.\n'
            'Hello World 3 times!\n'
            'We are done.\n')
