#! /usr/bin/env python

from startup import *
from mrd.subject_field import SubjectField

## Test SubjectField class

class TestSubjectFieldFunctions(unittest.TestCase):

    def setUp(self):
        # Instantiate a SubjectField object
        self.subject_field = SubjectField()

    def tearDown(self):
        # Release instantiated objects
        del self.subject_field

    def test_init(self):
        self.assertIsNone(self.subject_field.language)
        self.assertIsNone(self.subject_field.semanticDomain)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSubjectFieldFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
