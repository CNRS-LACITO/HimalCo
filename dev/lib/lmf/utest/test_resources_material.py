#! /usr/bin/env python

from startup import *
from resources.material import Material

## Test Material class

class TestMaterialFunctions(unittest.TestCase):

    def setUp(self):
        # Instantiate a Material object
        self.material = Material()

    def tearDown(self):
        # Release instantiated objects
        del self.material

    def test_init(self):
        self.assertIsNone(self.material.mediaType)
        self.assertIsNone(self.material.fileName)
        self.assertIsNone(self.material.author)

suite = unittest.TestLoader().loadTestsFromTestCase(TestMaterialFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
