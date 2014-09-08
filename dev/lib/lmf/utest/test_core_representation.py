#! /usr/bin/env python

from startup import *
from core.representation import Representation

## Test Representation class

class TestRepresentationFunctions(unittest.TestCase):

    def setUp(self):
        # Instantiate a Representation object
        self.representation = Representation()

    def tearDown(self):
        # Release instantiated objects
        del self.representation

    def test_init(self):
        self.assertIsNone(self.representation.comment)
        self.assertIsNone(self.representation.writtenForm)
        self.assertIsNone(self.representation.language)

suite = unittest.TestLoader().loadTestsFromTestCase(TestRepresentationFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
