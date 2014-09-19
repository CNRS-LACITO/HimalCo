#! /usr/bin/env python

from startup import *
from core.lexicon import Lexicon
from core.lexical_entry import LexicalEntry

## Test Lexicon class

class TestLexiconFunctions(unittest.TestCase):

    def setUp(self):
        # Instantiate a Lexicon object
        self.lexicon = Lexicon()

    def tearDown(self):
        # Release instantiated objects
        del self.lexicon

    def test_init(self):
        self.assertIsNone(self.lexicon.language)
        self.assertIsNone(self.lexicon.languageScript)
        self.assertIsNone(self.lexicon.id)
        self.assertIsNone(self.lexicon.label)
        self.assertIsNone(self.lexicon.lexiconType)
        self.assertIsNone(self.lexicon.entrySource)
        self.assertIsNone(self.lexicon.vowelHarmony)
        self.assertListEqual(self.lexicon.lexical_entry, [])

    def test_get_lexical_entries(self):
        # Create lexical entries
        entry1 = LexicalEntry()
        entry2 = LexicalEntry()
        # Add entries to the lexicon
        self.lexicon.lexical_entry = [entry1, entry2]
        # Test get lexical entries
        self.assertEqual(self.lexicon.get_lexical_entries(), set([entry1, entry2]))
        self.lexicon.lexical_entry.append(entry1)
        self.assertEqual(self.lexicon.get_lexical_entries(), set([entry1, entry2]))
        # Release LexicalEntry instances
        del self.lexicon.lexical_entry[:]
        del entry1, entry2

    def test_add_lexical_entry(self):
        # Create lexical entries
        entry1 = LexicalEntry()
        entry2 = LexicalEntry()
        # Test add entries to the lexicon
        self.assertEqual(self.lexicon.add_lexical_entry(entry1), self.lexicon)
        self.assertListEqual(self.lexicon.lexical_entry, [entry1])
        self.assertEqual(self.lexicon.add_lexical_entry(entry2), self.lexicon)
        self.assertListEqual(self.lexicon.lexical_entry, [entry1, entry2])
        # Release LexicalEntry instances
        del self.lexicon.lexical_entry[:]
        del entry1, entry2

    def test_remove_lexical_entry(self):
        # Create lexical entries
        entry1 = LexicalEntry()
        entry2 = LexicalEntry()
        # Add entries to the lexicon
        self.lexicon.lexical_entry = [entry1, entry2]
        # Test remove lexical entries
        self.assertEqual(self.lexicon.remove_lexical_entry(entry1), self.lexicon)
        self.assertListEqual(self.lexicon.lexical_entry, [entry2])
        self.assertEqual(self.lexicon.remove_lexical_entry(entry2), self.lexicon)
        self.assertListEqual(self.lexicon.lexical_entry, [])
        # Release LexicalEntry instances
        del entry1, entry2

    def test_count_lexical_entries(self):
        # Create lexical entries
        entry1 = LexicalEntry()
        entry2 = LexicalEntry()
        # Add entries to the lexicon
        self.lexicon.lexical_entry = [entry1]
        # Test count lexical entries
        self.assertEqual(self.lexicon.count_lexical_entries(), 1)
        self.lexicon.lexical_entry.append(entry2)
        self.assertEqual(self.lexicon.count_lexical_entries(), 2)
        self.lexicon.lexical_entry.append(entry1)
        self.assertEqual(self.lexicon.count_lexical_entries(), 2)
        # Release LexicalEntry instances
        del self.lexicon.lexical_entry[:]
        del entry1, entry2

    def test_sort_lexical_entries(self):
        # Create several lexical entries with different lexemes
        entry1 = LexicalEntry().set_lexeme("aa")
        entry2 = LexicalEntry().set_lexeme("ab")
        entry3 = LexicalEntry().set_lexeme("ba")
        entry4 = LexicalEntry().set_lexeme("bb")
        # Add entries to the lexicon
        self.lexicon.lexical_entry = [entry4, entry1, entry2, entry3]
        # Test sort lexical entries
        self.assertListEqual(self.lexicon.sort_lexical_entries(), [entry1, entry2, entry3, entry4])
        # Release LexicalEntry instances
        del self.lexicon.lexical_entry[:]
        del entry1, entry2, entry3, entry4

    def test_find_lexical_entries(self):
        # Create several lexical entries with different lexemes
        entry1 = LexicalEntry().set_lexeme("Hello")
        entry2 = LexicalEntry().set_lexeme("world!")
        entry3 = LexicalEntry().set_lexeme("hello")
        entry4 = LexicalEntry().set_lexeme("world")
        # Add entries to the lexicon
        self.lexicon.lexical_entry = [entry1, entry2, entry3, entry4]
        # Test find lexical entries
        self.assertListEqual(self.lexicon.find_lexical_entries(lambda entry: entry.get_lexeme() == "Hello"), [entry1])
        def test_filter(entry):
            return entry.get_lexeme().lower() == "hello"
        self.assertListEqual(self.lexicon.find_lexical_entries(test_filter), [entry1, entry3])
        # Release LexicalEntry instances
        del self.lexicon.lexical_entry[:]
        del entry1, entry2, entry3, entry4

    def test_check_cross_references(self):
        pass

    def test_convert_to_latex(self):
        pass

suite = unittest.TestLoader().loadTestsFromTestCase(TestLexiconFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
