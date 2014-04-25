from tests.system.test_tasks import BaseTasksTest

class VarsTest(BaseTasksTest):
    
    #Public
    
    __test__ = True
    
    #Protected
    
    @property
    def _filename(self):
        return 'vars.py'