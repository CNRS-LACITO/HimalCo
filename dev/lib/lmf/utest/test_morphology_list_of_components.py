#! /usr/bin/env python

from startup import *
from morphology.list_of_components import ListOfComponents

## Test ListOfComponents class

class TestListOfComponentsFunctions(unittest.TestCase):

    def setUp(self):
        # Instantiate a ListOfComponents object
        self.list_of_components = ListOfComponents()

    def tearDown(self):
        # Release instantiated objects
        del self.list_of_components

    def test_init(self):
        pass

suite = unittest.TestLoader().loadTestsFromTestCase(TestListOfComponentsFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
