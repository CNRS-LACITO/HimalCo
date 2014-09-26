#! /usr/bin/env python

from startup import *
from morphology.word_form import WordForm

## Test WordForm class

class TestWordFormFunctions(unittest.TestCase):

    def setUp(self):
        # Instantiate a WordForm object
        self.word_form = WordForm()

    def tearDown(self):
        # Release instantiated objects
        del self.word_form

    def test_init(self):
        self.assertIsNone(self.word_form.variantForm)
        self.assertIsNone(self.word_form.type)
        self.assertListEqual(self.word_form.form_representation, [])
        self.assertIsNone(self.word_form.grammaticalNumber)
        self.assertIsNone(self.word_form.grammaticalGender)
        self.assertIsNone(self.word_form.person)
        self.assertIsNone(self.word_form.anymacy)
        self.assertIsNone(self.word_form.clusivity)
        self.assertIsNone(self.word_form.tense)
        self.assertIsNone(self.word_form.case)
        self.assertIsNone(self.word_form.degree)
        self.assertIsNone(self.word_form.voice)
        self.assertIsNone(self.word_form.verbFormMood)

suite = unittest.TestLoader().loadTestsFromTestCase(TestWordFormFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
