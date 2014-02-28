#! /usr/bin/env python
# -*- coding: utf-8 -*-

from startup import *

# Remove the other mdf2xml_tb module
if 'mdf2xml_tb' in sys.modules:
    del(sys.modules["mdf2xml_tb"])
try:
    sys.path.remove("./xls2xml/py")
except ValueError:
    pass
# Import mdf2xml_tb
sys.path.append("./mdf2xml/py")
from mdf2xml_tb import *

## Test Mdf2Xml class

class TestMdf2XmlFunctions(unittest.TestCase):

    def setUp(self):
        # Instantiate an Mdf2Xml object
        self.mdf2xml = Mdf2Xml()
        self.mdf2xml.options = Options()
        self.mdf2xml.options.input = "obj/test_file.mdf"

    def tearDown(self):
        # Release instantiated objects
        del self.mdf2xml.options, self.mdf2xml

    def test_init(self):
        self.assertIsNone(self.mdf2xml.first_element)
        self.assertIsNone(self.mdf2xml.tree)

    def test_parse_options(self):
        self.mdf2xml.parse_options()
        self.assertFalse(self.mdf2xml.options.verbose)
        self.assertEqual(self.mdf2xml.options.input, "../../dict/japhug/toolbox/Dictionary.txt")
        self.assertEqual(self.mdf2xml.options.output, "./obj/Dictionary.xml")
        self.assertEqual(self.mdf2xml.options.database, "../../dict/japhug/lexique_pro/japhug.db")
        self.assertEqual(self.mdf2xml.options.grammar, GRAMMAR_JAP1)
        self.assertEqual(self.mdf2xml.options.struct, "../../dict/japhug/toolbox/Settings/MDF_AltH.typ")
        self.assertIsNone(self.mdf2xml.options.test)
        #self.assertTrue(self.mdf2xml.options.unit_test)

    def test_format_lx(self):
        in_lines = ["\lx _a\n", "\lx ^ab\n", "\lx $abc\n"]
        expected_lines = ["\lx a\n", "\lx ab\n", "\lx abc\n"]
        for i in range (0,3):
            self.assertEqual(self.mdf2xml.format_lx(in_lines[i]), expected_lines[i])

    def test_format_pd(self):
        in_lines = ["\\1s blabla\n", "\\4s blabla\n", "\pd blabla\n"]
        expected_lines = ["\\a1s blabla\n", "\\a4s blabla\n", "\pd blabla\n"]
        for i in range (0,3):
            self.assertEqual(self.mdf2xml.format_pd(in_lines[i]), expected_lines[i])

    def test_main(self):
        import os
        # Write input MDF file
        test_file = self.mdf2xml.open_write(self.mdf2xml.options.input)
        test_file.write("\_sh v3.0  123  MDF 4.0\n\_DateStampHasFourDigitYear\n\n")
        test_file.write("\lx hello\n\\test toto\n")
        test_file.close()
        # Set corret command line arguments
        sys.argv.append('-i')
        sys.argv.append(self.mdf2xml.options.input)
        sys.argv.append('-g')
        sys.argv.append(r"""lxGroup : {<lx><test>}""")
        # Run main
        self.mdf2xml.main()
        # Remove command line arguments
        for i in range (0, 4):
            sys.argv.pop()
        # Remove generated files
        os.remove(self.mdf2xml.options.input)
        os.remove("obj/test_file.xml")

suite = unittest.TestLoader().loadTestsFromTestCase(TestMdf2XmlFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
