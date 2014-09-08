#! /usr/bin/env python

from startup import *
from morphology.lemma import Lemma

## Test Lemma class

class TestLemmaFunctions(unittest.TestCase):

    def setUp(self):
        # Instantiate a Lemma object
        self.lemma = Lemma()

    def tearDown(self):
        # Release instantiated objects
        del self.lemma

    def test_init(self):
        self.assertIsNone(self.lemma.hyphenation)
        self.assertIsNone(self.lemma.lexeme)

    def test_set_lexeme(self):
        lexeme = "This is a lexeme."
        self.assertEqual(self.lemma.set_lexeme(lexeme), self.lemma)
        self.assertEqual(self.lemma.lexeme, lexeme)

    def test_get_lexeme(self):
        lexeme = "My lexeme."
        self.lemma.lexeme = lexeme
        self.assertEqual(self.lemma.get_lexeme(), lexeme)

suite = unittest.TestLoader().loadTestsFromTestCase(TestLemmaFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
