#! /usr/bin/env python

from startup import *
from core.statement import Statement

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

suite = unittest.TestLoader().loadTestsFromTestCase(TestStatementFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
