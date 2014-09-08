#! /usr/bin/env python

from startup import *
from resources.human_resource import HumanResource

## Test HumanResource class

class TestHumanResourceFunctions(unittest.TestCase):

    def setUp(self):
        # Instantiate a HumanResource object
        self.human_resource = HumanResource()

    def tearDown(self):
        # Release instantiated objects
        del self.human_resource

    def test_init(self):
        self.assertIsNone(self.human_resource.name)
        self.assertIsNone(self.human_resource.anonymizationFlag)
        self.assertIsNone(self.human_resource.reference)
        self.assertIsNone(self.human_resource.source)

suite = unittest.TestLoader().loadTestsFromTestCase(TestHumanResourceFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
