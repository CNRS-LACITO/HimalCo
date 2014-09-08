#! /usr/bin/env python

from startup import *
from core.global_information import GlobalInformation

## Test GlobalInformation class

class TestGlobalInformationFunctions(unittest.TestCase):

    def setUp(self):
        # Instantiate a GlobalInformation object
        self.global_information = GlobalInformation()

    def tearDown(self):
        # Release instantiated objects
        del self.global_information

    def test_init(self):
        self.assertIsNone(self.global_information.languageCode)
        self.assertIsNone(self.global_information.author)
        self.assertIsNone(self.global_information.version)
        self.assertIsNone(self.global_information.lastUpdate)
        self.assertIsNone(self.global_information.license)
        self.assertIsNone(self.global_information.characterEncoding)
        self.assertIsNone(self.global_information.dateCoding)
        self.assertIsNone(self.global_information.creationDate)
        self.assertIsNone(self.global_information.projectName)
        self.assertIsNone(self.global_information.description)
        self.assertIsNone(self.global_information.bibliographicCitation)

suite = unittest.TestLoader().loadTestsFromTestCase(TestGlobalInformationFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
