#! /usr/bin/env python

from startup import *
from morphology.component import Component

## Test Component class

class TestComponentFunctions(unittest.TestCase):

    def setUp(self):
        # Instantiate a Component object
        self.component = Component()

    def tearDown(self):
        # Release instantiated objects
        del self.component

    def test_init(self):
        self.assertIsNone(self.component.position)

suite = unittest.TestLoader().loadTestsFromTestCase(TestComponentFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
