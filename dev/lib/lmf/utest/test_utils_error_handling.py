#! /usr/bin/env python

from startup import *
from utils.error_handling import ErrorHandling

## Test ErrorHandling class

class TestErrorHandlingFunctions(unittest.TestCase):

    def setUp(self):
        # Instantiate an ErrorHandling object
        self.error_handling = ErrorHandling()

    def tearDown(self):
        # Release instantiated objects
        del self.error_handling

    def test_init(self):
        pass

suite = unittest.TestLoader().loadTestsFromTestCase(TestErrorHandlingFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
