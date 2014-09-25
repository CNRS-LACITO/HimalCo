#! /usr/bin/env python

from startup import *
from core.sense import Sense

## Test Sense class

class TestSenseFunctions(unittest.TestCase):

    def setUp(self):
        # Instantiate a Sense object
        self.sense = Sense()

    def tearDown(self):
        # Release instantiated objects
        del self.sense

    def test_init(self):
        self.assertIsNone(self.sense.senseNumber)
        self.assertIsNone(self.sense.id)
        self.assertListEqual(self.sense.definition, [])
        self.assertListEqual(self.sense.sense, [])
        self.assertListEqual(self.sense.equivalent, [])
        self.assertListEqual(self.sense.context, [])
        self.assertListEqual(self.sense.subject_field, [])
        self.assertListEqual(self.sense.paradigm, [])

suite = unittest.TestLoader().loadTestsFromTestCase(TestSenseFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
