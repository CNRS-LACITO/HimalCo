#! /usr/bin/env python

from startup import *
from core.definition import Definition

## Test Definition class

class TestDefinitionFunctions(unittest.TestCase):

    def setUp(self):
        # Instantiate a Definition object
        self.definition = Definition()

    def tearDown(self):
        # Release instantiated objects
        del self.definition

    def test_init(self):
        self.assertIsNone(self.definition.language)
        self.assertIsNone(self.definition.definition)
        self.assertIsNone(self.definition.gloss)
        self.assertIsNone(self.definition.literally)

suite = unittest.TestLoader().loadTestsFromTestCase(TestDefinitionFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
