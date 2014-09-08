#! /usr/bin/env python

from startup import *
from morphology.related_form import RelatedForm

## Test RelatedForm class

class TestRelatedFormFunctions(unittest.TestCase):

    def setUp(self):
        # Instantiate a RelatedForm object
        self.related_form = RelatedForm()

    def tearDown(self):
        # Release instantiated objects
        del self.related_form

    def test_init(self):
        self.assertIsNone(self.related_form.semanticRelation)

suite = unittest.TestLoader().loadTestsFromTestCase(TestRelatedFormFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
