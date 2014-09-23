#! /usr/bin/env python

from startup import *
from output.xml_lmf import xml_lmf_write, build_sub_elements
from core.lexical_entry import LexicalEntry
from morphology.lemma import Lemma
from utils.xml_format import Element, SubElement

## Test XML LMF functions

class TestXmlLmfFunctions(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_xml_lmf_write(self):
        import sys, os
        # Create LMF objects
        lexical_entry = LexicalEntry()
        lexical_entry.lemma = Lemma()
        lexical_entry.partOfSpeech = "toto"
        lexical_entry.status = "draft"
        lexical_entry.lemma.lexeme = "hello"
        # Write XML LMF file and test result
        utest_path = sys.path[0] + '/'
        xml_lmf_filename = utest_path + "lmf_output.xml"
        xml_lmf_write(lexical_entry, xml_lmf_filename)
        xml_lmf_file = open(xml_lmf_filename, "r")
        if os.name == 'posix':
            # Unix-style end of line
            eol = '\n'
        else:
            # Windows-style end of line
            eol = '\r\n'
        expected_lines = ["""<?xml version="1.0" ?>""" + eol,
            """<LexicalEntry id="0">""" + eol,
            """    <feat att="status" val="draft"/>""" + eol,
            """    <Lemma>""" + eol,
            """        <feat att="lexeme" val="hello"/>""" + eol,
            """    </Lemma>""" + eol,
            """    <feat att="partOfSpeech" val="toto"/>""" + eol,
            """</LexicalEntry>""" + eol]
        self.assertListEqual(expected_lines, xml_lmf_file.readlines())
        xml_lmf_file.close()
        del lexical_entry.lemma, lexical_entry
        # Remove XML LMF file
        os.remove(xml_lmf_filename)

    def test_build_sub_elements(self):
        # Create LMF objects and an empty XML element
        instance = LexicalEntry()
        instance.lemma = Lemma()
        instance.partOfSpeech = "toto"
        instance.status = "draft"
        instance.lemma.lexeme = "hello"
        element = Element("LexicalEntry")
        # Build sub-elements and test result
        build_sub_elements(instance, element)
        lemma = element.find("Lemma")
        lexeme = lemma.find("feat")
        self.assertEqual(lexeme.attrib["att"], "lexeme")
        self.assertEqual(lexeme.attrib["val"], "hello")
        [status, partOfSpeech] = element.findall("feat")
        self.assertEqual(partOfSpeech.attrib["att"], "partOfSpeech")
        self.assertEqual(partOfSpeech.attrib["val"], "toto")
        self.assertEqual(status.attrib["att"], "status")
        self.assertEqual(status.attrib["val"], "draft")
        del instance.lemma, instance, element

suite = unittest.TestLoader().loadTestsFromTestCase(TestXmlLmfFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
