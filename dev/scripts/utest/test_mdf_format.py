#! /usr/bin/env python
# -*- coding: utf-8 -*-

from startup import *

try:
    from xml.etree.cElementTree import Element, SubElement, ElementTree, tostring
except ImportError:
    from xml.etree.ElementTree import Element, SubElement, ElementTree, tostring

## Test MdfFormat class

class TestMdfFormatFunctions(unittest.TestCase):

    def setUp(self):
        # Instantiate an MdfFormat object
        self.mdf_format = MdfFormat()
        self.mdf_format.options = Options()
        self.mdf_format.options.input = "obj/test_file.mdf"
        self.mdf_format.options.grammar = r"""lxGroup : {<lx><test>}"""

    def tearDown(self):
        # Release instantiated objects
        del self.mdf_format.options
        del self.mdf_format

    def test_init(self):
        self.assertIsNone(self.mdf_format.first_element)
        self.assertIsNone(self.mdf_format.tree)

    def test_process_data(self):
        import os
        # Write input MDF file
        in_out = InOut()
        test_file = in_out.open_write(self.mdf_format.options.input)
        test_file.write("\_sh v3.0  123  MDF 4.0\n\_DateStampHasFourDigitYear\n\n")
        test_file.write("\lx hello\n\\test toto\n")
        test_file.close()
        del in_out
        # Build expected XML result
        tb_data = Element("toolbox_data")
        header = SubElement(tb_data, "header")
        sh = SubElement(header, "_sh")
        sh.text = "v3.0  123  MDF 4.0"
        lx_group = SubElement(tb_data, "lxGroup")
        lx = SubElement(lx_group, "lx")
        lx.text = "hello"
        test = SubElement(lx_group, "test")
        test.text = "toto"
        tree = ElementTree(element=tb_data)
        # Process with NLTK
        self.mdf_format.process_data()
        # Test XML result
        self.assertEqual(tostring(self.mdf_format.first_element), tostring(tb_data))
        # Remove input file
        os.system("rm " + self.mdf_format.options.input)
        # Release
        del tree, tb_data

suite = unittest.TestLoader().loadTestsFromTestCase(TestMdfFormatFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
