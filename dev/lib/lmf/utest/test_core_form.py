#! /usr/bin/env python

from startup import *
from core.form import Form

## Test Form class

class TestFormFunctions(unittest.TestCase):

    def setUp(self):
        # Instantiate a Form object
        self.form = Form()

    def tearDown(self):
        # Release instantiated objects
        del self.form

    def test_init(self):
        self.assertIsNone(self.form.variantForm)
        self.assertIsNone(self.form.type)

suite = unittest.TestLoader().loadTestsFromTestCase(TestFormFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
