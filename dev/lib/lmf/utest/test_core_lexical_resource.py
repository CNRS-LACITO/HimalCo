#! /usr/bin/env python

from startup import *
from core.lexical_resource import LexicalResource
from core.lexicon import Lexicon
from core.global_information import GlobalInformation

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
        self.assertIsInstance(self.lexical_resource.global_information, GlobalInformation)
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

    def test_set_creationDate(self):
        date = "2014-10-08"
        self.assertEqual(self.lexical_resource.set_creationDate(date), self.lexical_resource)
        self.assertEqual(self.lexical_resource.global_information.creationDate, date)

    def test_get_creationDate(self):
        self.assertEqual(self.lexical_resource.get_creationDate(), self.lexical_resource.global_information.creationDate)

    def test_set_lastUpdate(self):
        date = "2014-10-10"
        self.assertEqual(self.lexical_resource.set_lastUpdate(date), self.lexical_resource)
        self.assertEqual(self.lexical_resource.global_information.lastUpdate, date)

    def test_get_lastUpdate(self):
        self.assertEqual(self.lexical_resource.get_lastUpdate(), self.lexical_resource.global_information.lastUpdate)

    def test_set_author(self):
        author = "My Name"
        self.assertEqual(self.lexical_resource.set_author(author), self.lexical_resource)
        self.assertEqual(self.lexical_resource.global_information.author, author)

    def test_get_author(self):
        self.assertEqual(self.lexical_resource.get_author(), self.lexical_resource.global_information.author)

    def test_set_description(self):
        descr = "This is a short description of this lexical resource."
        self.assertEqual(self.lexical_resource.set_description(descr), self.lexical_resource)
        self.assertEqual(self.lexical_resource.global_information.description, descr)

    def test_get_description(self):
        self.assertEqual(self.lexical_resource.get_description(), self.lexical_resource.global_information.description)

    def test_get_bibliographicCitation(self):
        self.assertEqual(self.lexical_resource.get_bibliographicCitation(), self.lexical_resource.global_information.bibliographicCitation)

suite = unittest.TestLoader().loadTestsFromTestCase(TestLexicalResourceFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
