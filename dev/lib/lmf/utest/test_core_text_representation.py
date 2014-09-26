#! /usr/bin/env python

from startup import *
from core.text_representation import TextRepresentation

## Test TextRepresentation class

class TestTextRepresentationFunctions(unittest.TestCase):

    def setUp(self):
        # Instantiate a TextRepresentation object
        self.text_representation = TextRepresentation()

    def tearDown(self):
        # Release instantiated objects
        del self.text_representation

    def test_init(self):
        self.assertIsNone(self.text_representation.comment)
        self.assertIsNone(self.text_representation.writtenForm)
        self.assertIsNone(self.text_representation.language)
        self.assertIsNone(self.text_representation.font)

suite = unittest.TestLoader().loadTestsFromTestCase(TestTextRepresentationFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
