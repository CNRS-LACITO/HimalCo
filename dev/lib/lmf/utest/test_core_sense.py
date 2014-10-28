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
        self.assertEqual(self.sense.id, 0)
        self.assertListEqual(self.sense.definition, [])
        self.assertListEqual(self.sense.sense, [])
        self.assertListEqual(self.sense.equivalent, [])
        self.assertListEqual(self.sense.context, [])
        self.assertListEqual(self.sense.subject_field, [])
        self.assertListEqual(self.sense.paradigm, [])

    def test_get_id(self):
        self.assertIs(self.sense.get_id(), self.sense.id)

    def test_set_senseNumber(self):
        nb = 123
        self.assertIs(self.sense.set_senseNumber(nb), self.sense)
        self.assertEqual(self.sense.senseNumber, nb)

    def test_get_senseNumner(self):
        nb = 456
        self.sense.senseNumber = nb
        self.assertEqual(self.sense.get_senseNumber(), nb)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSenseFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
