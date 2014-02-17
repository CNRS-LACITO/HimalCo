#! /usr/bin/env python
# -*- coding: utf-8 -*-

from startup import *

try:
    from xml.etree.cElementTree import Element, SubElement, ElementTree
except ImportError:
    from xml.etree.ElementTree import Element, SubElement, ElementTree

## Test XmlFormat class

class TestXmlFormatFunctions(unittest.TestCase):

    def setUp(self):
        # Instantiate an XmlFormat object
        self.xml_format = XmlFormat()
        self.xml_format.options = Options()
        self.xml_format.options.output = "obj/test_file.xml"
        self.xml_format.options.verbose = False
        self.xml_format.first_element = Element("top")
        # Add a subelement
        SubElement(self.xml_format.first_element, "under")

    def tearDown(self):
        # Release instantiated objects
        del self.xml_format.first_element, self.xml_format.options, self.xml_format

    def test_init(self):
        self.assertIsNone(self.xml_format.tree)

    def test_dump(self):
        self.xml_format.dump()

    def test_prettify(self):
        # Build expected result
        expected_str = u"<?xml version=\"1.0\" ?>\n<top>\n    <under/>\n</top>\n"
        # Test
        self.assertEqual(self.xml_format.prettify(self.xml_format.first_element), expected_str)

    def test_write_xml(self):
        import os
        self.xml_format.tree = ElementTree(element=self.xml_format.first_element)
        self.xml_format.write_xml()
        del self.xml_format.tree
        os.system("rm " + self.xml_format.options.output)

    def test_write_result(self):
        import os
        self.xml_format.write_result()
        os.system("rm " + self.xml_format.options.output)

    def test_display_result(self):
        self.xml_format.tree = ElementTree(element=self.xml_format.first_element)
        self.xml_format.display_result()
        del self.xml_format.tree

    def test_parse_xml(self):
        self.xml_format.tree = ElementTree(element=self.xml_format.first_element)
        self.xml_format.write_xml()
        self.xml_format.parse_xml(self.xml_format.options.output)
        del self.xml_format.tree

suite = unittest.TestLoader().loadTestsFromTestCase(TestXmlFormatFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
