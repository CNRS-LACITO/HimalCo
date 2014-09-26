#! /usr/bin/env python

from startup import *
from core.form_representation import FormRepresentation

## Test FormRepresentation class

class TestFormRepresentationFunctions(unittest.TestCase):

    def setUp(self):
        # Instantiate a FormRepresentation object
        self.form_representation = FormRepresentation()

    def tearDown(self):
        # Release instantiated objects
        del self.form_representation

    def test_init(self):
        self.assertIsNone(self.form_representation.comment)
        self.assertIsNone(self.form_representation.writtenForm)
        self.assertIsNone(self.form_representation.language)
        self.assertIsNone(self.form_representation.transliteration)
        self.assertIsNone(self.form_representation.tone)
        self.assertIsNone(self.form_representation.geographicalVariant)
        self.assertIsNone(self.form_representation.phoneticForm)
        self.assertIsNone(self.form_representation.contextualVariation)
        self.assertIsNone(self.form_representation.spellingVariant)
        self.assertIsNone(self.form_representation.citationForm)
        self.assertIsNone(self.form_representation.dialect)
        self.assertIsNone(self.form_representation.language)
        self.assertIsNone(self.form_representation.scriptName)
        self.assertListEqual(self.form_representation.audio, [])
        self.assertIsNone(self.form_representation.targets)
        self.assertListEqual(self.form_representation.get_speakers(), [])

suite = unittest.TestLoader().loadTestsFromTestCase(TestFormRepresentationFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
