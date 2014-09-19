#! /usr/bin/env python

from startup import *
from core.lexical_entry import LexicalEntry
from morphology.lemma import Lemma

## Test LexicalEntry class

class TestLexicalEntryFunctions(unittest.TestCase):

    def setUp(self):
        # Instantiate a LexicalEntry object
        self.lexical_entry = LexicalEntry()

    def tearDown(self):
        # Release instantiated objects
        del self.lexical_entry

    def test_init(self):
        self.assertIsNone(self.lexical_entry.homonymNumber)
        self.assertIsNone(self.lexical_entry.status)
        self.assertIsNone(self.lexical_entry.date)
        self.assertIsNone(self.lexical_entry.partOfSpeech)
        self.assertIsNone(self.lexical_entry.independentWord)
        self.assertIsNone(self.lexical_entry.bibliography)
        self.assertEqual(self.lexical_entry.id, 0)
        self.assertIsNone(self.lexical_entry.lemma)

    def test_set_partOfSpeech(self):
        part_of_speech = "verb"
        self.assertEqual(self.lexical_entry.set_partOfSpeech(part_of_speech), self.lexical_entry)
        self.assertEqual(self.lexical_entry.partOfSpeech, part_of_speech)

    def test_get_partOfSpeech(self):
        self.assertEqual(self.lexical_entry.get_partOfSpeech(), self.lexical_entry.partOfSpeech)

    def test_set_status(self):
        status = "draft"
        self.assertEqual(self.lexical_entry.set_status(status), self.lexical_entry)
        self.assertEqual(self.lexical_entry.status, status)

    def test_get_status(self):
        self.assertEqual(self.lexical_entry.get_status(), self.lexical_entry.status)

    def test_get_id(self):
        self.assertEqual(self.lexical_entry.get_id(), self.lexical_entry.id)

    def test_set_lexeme(self):
        lexeme = "hello"
        self.assertEqual(self.lexical_entry.set_lexeme(lexeme), self.lexical_entry)
        self.assertEqual(self.lexical_entry.lemma.lexeme, lexeme)

    def test_get_lexeme(self):
        # There is no Lemma instance
        self.assertIsNone(self.lexical_entry.get_lexeme())
        # Create a Lemma instance
        self.lexical_entry.lemma = Lemma()
        self.assertEqual(self.lexical_entry.get_lexeme(), self.lexical_entry.lemma.lexeme)
        # Delete Lemma instance
        del self.lexical_entry.lemma

    def test_get_definitions(self):
        pass

    def test_get_senses(self):
        pass

    def test_get_gloss(self):
        pass

suite = unittest.TestLoader().loadTestsFromTestCase(TestLexicalEntryFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
