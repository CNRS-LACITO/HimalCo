#! /usr/bin/env python
# -*- coding: utf-8 -*-

from startup import *

# Remove the other mdf2xml_tb module
if 'mdf2xml_tb' in sys.modules:
    del(sys.modules["mdf2xml_tb"])
try:
    sys.path.remove("./mdf2xml/py")
except ValueError:
    pass
# Import xls2xml
sys.path.append("./xls2xml/py")
from xls2mdf import *
# Import mdf2xml_tb
from mdf2xml_tb import *

## Test Xls2Mdf class

class TestXls2MdfFunctions(unittest.TestCase):
    
    def setUp(self):
        import os
        # Instantiate an Xls2Mdf object
        self.xls2mdf = Xls2Mdf()
        self.xls2mdf.options = Options()
        self.xls2mdf.options.input = "./obj/test_file.xls"
        self.xls2mdf.options.output = "./obj/test_file.mdf"
        #os.system("cp test/na/input/na1.xls " + self.xls2mdf.options.input)
        # Write input file
        self.book = self.xls2mdf.create_book()
        self.sheet = self.book.add_sheet("sheet")
        self.sheet.write(0, 0, label="\lx")
        self.sheet.write(0, 1, label="\sf numbering=\"B\"")
        self.sheet.write(0, 2, label="\sf numbering=\"2011\"")
        self.sheet.write(1, 0, label="10")
        self.sheet.write(1, 1, label="11")
        self.sheet.write(1, 2, label="12")
        self.book.save(self.xls2mdf.options.input)

    def tearDown(self):
        import os
        os.system("rm " + self.xls2mdf.options.input)
        # Release instantiated objects
        del self.xls2mdf.options, self.xls2mdf

    def test_init(self):
        self.assertIsNone(self.xls2mdf.sheet)
        self.assertIsNone(self.xls2mdf.wb)
        self.assertIsNone(self.xls2mdf.tmp_filename)
        self.assertIsNone(self.xls2mdf.txt_filename)

    def test_parse_options(self):
        self.xls2mdf.parse_options()
        self.assertFalse(self.xls2mdf.options.verbose)
        self.assertEqual(self.xls2mdf.options.input, "../../dict/na/lexique_na_2013sq_POUR_TRANSFERT.xls")
        self.assertEqual(self.xls2mdf.options.output, "./obj/lexique_na_2013sq_POUR_TRANSFERT.mdf")
        self.assertEqual(self.xls2mdf.options.grammar, GRAMMAR_NA)
        self.assertIsNone(self.xls2mdf.options.test)
        #self.assertTrue(self.xls2mdf.options.unit_test)
        self.assertEqual(self.xls2mdf.tmp_filename, "./obj/lexique_na_2013sq_POUR_TRANSFERT.tmp")
        self.assertEqual(self.xls2mdf.txt_filename, "./obj/lexique_na_2013sq_POUR_TRANSFERT.txt")
        # For removal
        self.xls2mdf.options.input = "./obj/test_file.xls"

    def test_get_marker(self):
        self.xls2mdf.open_book()
        self.xls2mdf.get_sheet()
        self.assertEqual(self.xls2mdf.get_marker(1), "\sf")

    def test_display_markers(self):
        self.xls2mdf.open_book()
        self.xls2mdf.get_sheet()
        self.xls2mdf.display_markers()

    def test_write_fields(self):
        import os
        self.xls2mdf.tmp_filename = "./obj/test_file.tmp"
        self.xls2mdf.open_book()
        self.xls2mdf.get_sheet()
        self.xls2mdf.write_fields()
        # Build expected result
        lines = [u"\lx 10\n", u"\sf 11\n", u"\sf 12\n", u"\n"]
        output = self.xls2mdf.open_read(self.xls2mdf.tmp_filename)
        self.assertListEqual(output.readlines(), lines)
        output.close()
        os.system("rm " + self.xls2mdf.tmp_filename)

    def test_format_fields(self):
        import os
        # Write temporary file
        self.xls2mdf.tmp_filename = "./obj/test_file.tmp"
        tmp = self.xls2mdf.open_write(self.xls2mdf.tmp_filename)
        tmp.write("\lx toto\n")
        tmp.write("\lx tata_MAINENTRY\n")
        tmp.write("\\xv simple example\n")
        tmp.write("\\xf exemple simple\n")
        tmp.write("\\xv example1 <2>example2 <3>example 3\n")
        tmp.write("\\xf exemple1 <2>exemple2 <3>exemple 3\n")
        tmp.write("\lx tata_SUBENTRY\n")
        tmp.write("\\va variant (attention) (please)\n")
        tmp.close()
        # Build expected result
        lines = [u"\lx toto\n",
                 u"\lx tata\n",
                 u"\\xv simple example\n",
                 u"\\xf exemple simple\n",
                 u"\\xv example1\n",
                 u"\\xf exemple1\n",
                 u"\\xv example2\n",
                 u"\\xf exemple2\n",
                 u"\\xv example 3\n",
                 u"\\xf exemple 3\n",
                 u"\se tata\n",
                 u"\\va variant\n",
                 u"\\vf attention\n",
                 u"\\vf please\n"]
        # Run formatting
        self.xls2mdf.format_fields()
        # Check results
        output = self.xls2mdf.open_read(self.xls2mdf.options.output)
        self.assertListEqual(output.readlines(), lines)
        output.close()
        os.system("rm " + self.xls2mdf.tmp_filename + " " + self.xls2mdf.options.output)

    def test_remove_fields(self):
        import os
        # Write MDF file
        self.xls2mdf.txt_filename = "./obj/test_file.txt"
        mdf = self.xls2mdf.open_write(self.xls2mdf.options.output)
        mdf.write("\lx toto\n")
        mdf.write("\ms *\n")
        mdf.write("\\xv simple example\n")
        mdf.write("\\xf exemple simple\n")
        mdf.write("\n")
        mdf.write("\lx tata\n")
        mdf.write("\sf\n")
        mdf.write("\\va variant\n")
        mdf.close()
        # Build expected result
        lines = [u"\lx toto\n",
                 u"\\xv simple example\n",
                 u"\\xf exemple simple\n",
                 u"\n",
                 u"\lx tata\n",
                 u"\\va variant\n"]
        # Run removing
        self.xls2mdf.remove_fields()
        # Check results
        output = self.xls2mdf.open_read(self.xls2mdf.txt_filename)
        self.assertListEqual(output.readlines(), lines)
        output.close()
        os.system("rm " + self.xls2mdf.options.output + " " + self.xls2mdf.txt_filename)

    def test_format_lx(self):
        pass

    def test_format_example(self):
        pass

    def test_format_va(self):
        pass

    def test_main(self):
        import os
        # Set corret command line arguments
        sys.argv.append('-i')
        sys.argv.append(self.xls2mdf.options.input)
        sys.argv.append('-g')
        sys.argv.append(r"""lxGroup : {<lx><test>}""")
        # Run main
        self.xls2mdf.main()
        # Remove command line arguments
        for i in range (0, 4):
            sys.argv.pop()
        # Remove generated files
        os.system("rm obj/test_file.mdf")
        os.system("rm obj/test_file.txt")

suite = unittest.TestLoader().loadTestsFromTestCase(TestXls2MdfFunctions)

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
        self.assertEqual(self.mdf2xml.options.input, "../../dict/na/lexique_na_2013sq_POUR_TRANSFERT.xls")
        self.assertEqual(self.mdf2xml.options.output, "./obj/lexique_na_2013sq_POUR_TRANSFERT.xml")
        self.assertEqual(self.mdf2xml.options.grammar, GRAMMAR_NA)
        self.assertIsNone(self.mdf2xml.options.test)
        #self.assertTrue(self.mdf2xml.options.unit_test)

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
        os.system("rm " + self.mdf2xml.options.input)
        os.system("rm obj/test_file.xml")

suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMdf2XmlFunctions))

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
