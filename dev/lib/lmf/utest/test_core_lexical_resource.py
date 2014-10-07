#! /usr/bin/env python

from startup import *
from core.lexical_resource import LexicalResource
from core.lexicon import Lexicon

## Test LexicalResource class

class TestLexicalResourceFunctions(unittest.TestCase):

    def setUp(self):
        # Instantiate a LexicalResource object
        self.lexical_resource = LexicalResource()

    def tearDown(self):
        # Release instantiated objects
        del self.lexical_resource

    def test_init(self):
        self.assertEqual(self.lexical_resource.dtdVersion, 16)
        self.assertIsNone(self.lexical_resource.global_information)
        self.assertListEqual(self.lexical_resource.lexicon, [])
        self.assertListEqual(self.lexical_resource.speaker, [])

    def test_get_lexicons(self):
        # Create lexicons
        lexicon1 = Lexicon()
        lexicon2 = Lexicon()
        # Add lexicons to the lexical resource
        self.lexical_resource.lexicon = [lexicon1, lexicon2]
        # Test get lexicons
        self.assertListEqual(self.lexical_resource.get_lexicons(), [lexicon1, lexicon2])
        # Release Lexicon instances
        del self.lexical_resource.lexicon[:]
        del lexicon1, lexicon2

    def test_add_lexicon(self):
        # Create lexicons
        lexicon1 = Lexicon()
        lexicon2 = Lexicon()
        # Test add lexicons to the lexical resource
        self.assertEqual(self.lexical_resource.add_lexicon(lexicon1), self.lexical_resource)
        self.assertListEqual(self.lexical_resource.lexicon, [lexicon1])
        self.assertEqual(self.lexical_resource.add_lexicon(lexicon2), self.lexical_resource)
        self.assertListEqual(self.lexical_resource.lexicon, [lexicon1, lexicon2])
        # Release Lexicon instances
        del self.lexical_resource.lexicon[:]
        del lexicon1, lexicon2

    def test_remove_lexicon(self):
        # Create lexicons
        lexicon1 = Lexicon()
        lexicon2 = Lexicon()
        # Add lexicons to the lexical resource
        self.lexical_resource.lexicon = [lexicon1, lexicon2]
        # Test remove lexicons
        self.assertEqual(self.lexical_resource.remove_lexicon(lexicon1), self.lexical_resource)
        self.assertListEqual(self.lexical_resource.lexicon, [lexicon2])
        self.assertEqual(self.lexical_resource.remove_lexicon(lexicon2), self.lexical_resource)
        self.assertListEqual(self.lexical_resource.lexicon, [])
        # Release Lexicon instances
        del lexicon1, lexicon2

suite = unittest.TestLoader().loadTestsFromTestCase(TestLexicalResourceFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
