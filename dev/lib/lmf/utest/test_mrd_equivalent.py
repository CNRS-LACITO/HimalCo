#! /usr/bin/env python

from startup import *
from mrd.equivalent import Equivalent

## Test Equivalent class

class TestEquivalentFunctions(unittest.TestCase):

    def setUp(self):
        # Instantiate an Equivalent object
        self.equivalent = Equivalent()

    def tearDown(self):
        # Release instantiated objects
        del self.equivalent

    def test_init(self):
        self.assertIsNone(self.equivalent.language)
        self.assertIsNone(self.equivalent.translation)

suite = unittest.TestLoader().loadTestsFromTestCase(TestEquivalentFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
