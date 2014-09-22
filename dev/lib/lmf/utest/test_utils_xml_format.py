#! /usr/bin/env python

from startup import *
from utils.xml_format import prettify, write_result, parse_xml, Element, SubElement, ElementTree

## Test XML format functions

class TestXmlFormatFunctions(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_prettify(self):
        # Create XML element with sub-element
        element = Element("LexicalEntry")
        SubElement(element, "Lemma")
        # Build expected result
        import os
        if os.name == 'posix':
            # Linux-style end of line
            eol = u"\n"
        else:
            # Windows-style end of line
            eol = u"\r\n"
        expected_str = u"<?xml version=\"1.0\" ?>" + eol + u"<LexicalEntry>" + eol + u"    <Lemma/>" + eol + u"</LexicalEntry>" + eol
        # Test
        self.assertEqual(prettify(element), expected_str)
        del element

    def test_write_result(self):
        import sys, os
        utest_path = sys.path[0] + '/'
        xml_filename = utest_path + "output.xml"
        # Create XML element with sub-element
        element = Element("LexicalEntry")
        SubElement(element, "Lemma")
        # Write result
        write_result(element, xml_filename)
        del element
        # Remove XML file
        os.remove(xml_filename)

    def test_parse_xml(self):
        import sys, os
        utest_path = sys.path[0] + '/'
        xml_filename = utest_path + "input.xml"
        # Create XML tree
        element = Element("LexicalEntry")
        SubElement(element, "Lemma")
        tree = ElementTree(element)
        # Write tree then parse
        tree.write(xml_filename)
        parse_xml(xml_filename)
        del tree, element
        # Remove XML file
        os.remove(xml_filename)

suite = unittest.TestLoader().loadTestsFromTestCase(TestXmlFormatFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
