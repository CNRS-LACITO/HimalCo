#! /usr/bin/env python

from startup import *
from core.global_information import GlobalInformation
from utils.error_handling import Error

## Test GlobalInformation class

class TestGlobalInformationFunctions(unittest.TestCase):

    def setUp(self):
        # Instantiate a GlobalInformation object
        self.global_information = GlobalInformation()

    def tearDown(self):
        # Release instantiated objects
        del self.global_information

    def test_init(self):
        self.assertEqual(self.global_information.languageCode, "ISO-639-3")
        self.assertIsNone(self.global_information.author)
        self.assertEqual(self.global_information.version, "0.1")
        self.assertIsNone(self.global_information.lastUpdate)
        self.assertEqual(self.global_information.license, "GPL")
        self.assertEqual(self.global_information.characterEncoding, "UTF-8")
        self.assertEqual(self.global_information.dateCoding, "ISO-8601")
        self.assertIsNone(self.global_information.creationDate)
        self.assertEqual(self.global_information.projectName, "ANR HimalCo")
        self.assertIsNone(self.global_information.description)
        self.assertIsNone(self.global_information.bibliographicCitation)

    def test_set_creationDate(self):
        date = "2014-10-08"
        self.assertEqual(self.global_information.set_creationDate(date), self.global_information)
        self.assertEqual(self.global_information.creationDate, date)
        
    def test_get_creationDate(self):
        self.assertIs(self.global_information.get_creationDate(), self.global_information.creationDate)

    def test_set_lastUpdate(self):
        date = "2014-10-08"
        self.assertEqual(self.global_information.set_lastUpdate(date), self.global_information)
        self.assertEqual(self.global_information.lastUpdate, date)

    def test_get_lastUpdate(self):
        self.assertIs(self.global_information.get_lastUpdate(), self.global_information.lastUpdate)

    def test_set_author(self):
        author = "My Name"
        self.assertEqual(self.global_information.set_author(author), self.global_information)
        self.assertEqual(self.global_information.author, author)

    def test_get_author(self):
        self.assertIs(self.global_information.get_author(), self.global_information.author)

    def test_set_description(self):
        descr = "This is a short description of the lexical resource."
        self.assertEqual(self.global_information.set_description(descr), self.global_information)
        self.assertEqual(self.global_information.description, descr)

    def test_get_description(self):
        self.assertIs(self.global_information.get_description(), self.global_information.description)

    def test_compute_bibliographicCitation(self):
        self.global_information.author = "CNRS"
        self.global_information.lastUpdate = "2014"
        # Test compute bibliographic citation
        self.global_information.compute_bibliographicCitation()
        self.assertEqual(self.global_information.bibliographicCitation, "Online dictionaries, CNRS, 2014")

    def test_get_bibliographicCitation(self):
        self.assertIs(self.global_information.get_bibliographicCitation(), self.global_information.bibliographicCitation)

suite = unittest.TestLoader().loadTestsFromTestCase(TestGlobalInformationFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
