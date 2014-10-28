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
        self.assertListEqual(self.definition.text_representation, [])
        self.assertListEqual(self.definition.statement, [])

    def test_set_language(self):
        lang = "Python"
        self.assertIs(self.definition.set_language(lang), self.definition)
        self.assertEqual(self.definition.language, lang)

    def test_get_language(self):
        # Set language
        lang = "python"
        self.definition.language = lang
        # Test get language
        self.assertEqual(self.definition.get_language(), lang)

    def test_set_definition(self):
        # Test definition only
        definition = "blablabla"
        self.assertIs(self.definition.set_definition(definition), self.definition)
        self.assertEqual(self.definition.definition, definition)
        # Test definition and language
        definition = "This is a definition."
        language = "eng"
        self.assertIs(self.definition.set_definition(definition, language), self.definition)
        self.assertEqual(self.definition.definition, definition)
        self.assertEqual(self.definition.language, language)

    def test_get_definition(self):
        # Set definition
        definition = "whatever"
        self.definition.definition = definition
        # Test get definition
        self.assertEqual(self.definition.get_definition(), definition)
        # Test with a language filter
        language = "eng"
        self.definition.language = language
        self.assertEqual(self.definition.get_definition(), definition)
        self.assertIsNone(self.definition.get_definition("fra"))
        self.assertEqual(self.definition.get_definition(language), definition)

    def test_set_gloss(self):
        # Test gloss only
        gloss = "BLA"
        self.assertIs(self.definition.set_gloss(gloss), self.definition)
        self.assertEqual(self.definition.gloss, gloss)
        # Test gloss and language
        gloss = "This is a gloss."
        language = "eng"
        self.assertIs(self.definition.set_gloss(gloss, language), self.definition)
        self.assertEqual(self.definition.gloss, gloss)
        self.assertEqual(self.definition.language, language)

    def test_get_gloss(self):
        # Set gloss
        gloss = "WHATEVER"
        self.definition.gloss = gloss
        # Test get gloss
        self.assertEqual(self.definition.get_gloss(), gloss)
        # Test with a language filter
        language = "eng"
        self.definition.language = language
        self.assertEqual(self.definition.get_gloss(), gloss)
        self.assertIsNone(self.definition.get_gloss("fra"))
        self.assertEqual(self.definition.get_gloss(language), gloss)

suite = unittest.TestLoader().loadTestsFromTestCase(TestDefinitionFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
