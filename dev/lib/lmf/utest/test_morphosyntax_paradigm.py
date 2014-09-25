#! /usr/bin/env python

from startup import *
from morphosyntax.paradigm import Paradigm

## Test Paradigm class

class TestParadigmFunctions(unittest.TestCase):

    def setUp(self):
        # Instantiate a Paradigm object
        self.paradigm = Paradigm()

    def tearDown(self):
        # Release instantiated objects
        del self.paradigm

    def test_init(self):
        self.assertIsNone(self.paradigm.paradigmLabel)
        self.assertIsNone(self.paradigm.paradigm)
        self.assertIsNone(self.paradigm.language)
        self.assertIsNone(self.paradigm.morphology)
        self.assertIsNone(self.paradigm.get_lexical_entry())

suite = unittest.TestLoader().loadTestsFromTestCase(TestParadigmFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
