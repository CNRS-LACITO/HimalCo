#! /usr/bin/env python

from startup import *
from core.statement import Statement
from utils.error_handling import Error

## Test Statement class

class TestStatementFunctions(unittest.TestCase):

    def setUp(self):
        # Instantiate a Statement object
        self.statement = Statement()

    def tearDown(self):
        # Release instantiated objects
        del self.statement

    def test_init(self):
        self.assertIsNone(self.statement.noteType)
        self.assertIsNone(self.statement.note)
        self.assertIsNone(self.statement.language)
        self.assertIsNone(self.statement.encyclopedicInformation)
        self.assertIsNone(self.statement.usageNote)
        self.assertIsNone(self.statement.restriction)
        self.assertIsNone(self.statement.derivation)
        self.assertIsNone(self.statement.borrowedWord)
        self.assertIsNone(self.statement.writtenForm)
        self.assertIsNone(self.statement.sense)
        self.assertIsNone(self.statement.etymology)
        self.assertIsNone(self.statement.etymologyComment)
        self.assertIsNone(self.statement.etymologyGloss)
        self.assertIsNone(self.statement.etymologySource)
        self.assertIsNone(self.statement.termSourceLanguage)
        self.assertIsNone(self.statement.targetLexicalEntry)
        self.assertIsNone(self.statement.scientificName)
        self.assertListEqual(self.statement.text_representation, [])

    def test_set_note(self):
        # Test note only
        note = "blablabla"
        self.assertIs(self.statement.set_note(note), self.statement)
        self.assertEqual(self.statement.note, note)
        # Test note and type
        note = "This is a note."
        type = "discourse"
        self.assertIs(self.statement.set_note(note, type), self.statement)
        self.assertEqual(self.statement.note, note)
        self.assertEqual(self.statement.noteType, type)
        # Test note and language
        note = "This is another note."
        language = "eng"
        self.assertIs(self.statement.set_note(note, language=language), self.statement)
        self.assertEqual(self.statement.note, note)
        self.assertEqual(self.statement.language, language)
        # Test with type and language
        note = "note"
        type = "general"
        language = "fra"
        self.assertIs(self.statement.set_note(note, type, language), self.statement)
        self.assertEqual(self.statement.note, note)
        self.assertEqual(self.statement.noteType, type)
        self.assertEqual(self.statement.language, language)

    def test_get_note(self):
        # Set note
        note = "whatever"
        self.statement.note = note
        # Test get note
        self.assertEqual(self.statement.get_note(), note)
        # Test with a type filter
        type = "anthropology"
        self.statement.noteType = type
        self.assertIsNone(self.statement.get_note("sociolinguistics"))
        self.assertEqual(self.statement.get_note(type), note)
        # Test with a language filter
        language = "eng"
        self.statement.language = language
        self.assertIsNone(self.statement.get_note(language="fra"))
        self.assertEqual(self.statement.get_note(language=language), note)
        # Test with both filters
        type = "comment"
        language = "bla"
        self.statement.noteType = type
        self.statement.language = language
        self.assertIsNone(self.statement.get_note("usage", "eng"))
        self.assertIsNone(self.statement.get_note(type, "eng"))
        self.assertIsNone(self.statement.get_note("usage", language))
        self.assertEqual(self.statement.get_note(type, language), note)

    def test_set_language(self):
        lang = "Python"
        self.assertIs(self.statement.set_language(lang), self.statement)
        self.assertEqual(self.statement.language, lang)

    def test_get_language(self):
        # Set language
        lang = "python"
        self.statement.language = lang
        # Test get language
        self.assertEqual(self.statement.get_language(), lang)

    def test_set_noteType(self):
        # Test error case
        test = False
        try:
            self.statement.set_noteType("whatever")
        except Error:
            test = True
        self.assertTrue(test)
        # Test nominal case
        type = "phonology"
        self.assertIs(self.statement.set_noteType(type), self.statement)
        self.assertEqual(self.statement.noteType, type)

    def test_get_noteType(self):
        # Set note type
        type = "whatever"
        self.statement.noteType = type
        # Test get note type
        self.assertEqual(self.statement.get_noteType(), type)

suite = unittest.TestLoader().loadTestsFromTestCase(TestStatementFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
