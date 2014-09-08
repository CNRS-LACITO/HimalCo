#! /usr/bin/env python

from startup import *
from resources.resource import Resource

## Test Resource class

class TestResourceFunctions(unittest.TestCase):

    def setUp(self):
        # Instantiate a Resource object
        self.resource = Resource()

    def tearDown(self):
        # Release instantiated objects
        del self.resource

    def test_init(self):
        pass

suite = unittest.TestLoader().loadTestsFromTestCase(TestResourceFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
