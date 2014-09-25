#! /usr/bin/env python

from startup import *
from core.lexical_resource import LexicalResource

## Test LexicalResource class

class TestLexicalResourceFunctions(unittest.TestCase):

    def setUp(self):
        # Instantiate a LexicalResource object
        self.lexical_resource = LexicalResource()

    def tearDown(self):
        # Release instantiated objects
        del self.lexical_resource

    def test_init(self):
        self.assertIsNone(self.lexical_resource.dtdVersion)
        self.assertIsNone(self.lexical_resource.global_information)
        self.assertListEqual(self.lexical_resource.lexicon, [])
        self.assertListEqual(self.lexical_resource.speaker, [])

suite = unittest.TestLoader().loadTestsFromTestCase(TestLexicalResourceFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
