#! /usr/bin/env python

from startup import *
from input.mdf import mdf_read

## Test MDF functions

class TestMdfFunctions(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_mdf_read(self):
        import sys, os
        # Create an input MDF file
        utest_path = sys.path[0] + '/'
        mdf_filename = utest_path + "mdf_input.txt"
        mdf_file = open(mdf_filename, "w+")
        if os.name == 'posix':
            # Linux-style end of line
            eol = '\n'
        else:
            # Windows-style end of line
            eol = '\r\n'
        mdf_file.write("\\lx hello" + eol + "\\ps toto" + eol + "\\st draft" + eol)
        mdf_file.close()
        # Read MDF file and test result
        lexicon = mdf_read(mdf_filename)
        entry = lexicon.lexical_entry[0]
        self.assertEqual(entry.get_lexeme(), "hello")
        self.assertEqual(entry.get_partOfSpeech(), "toto")
        self.assertEqual(entry.get_status(), "draft")
        del entry, lexicon
        # Customize mapping
        mdf2lmf = dict({
            "lx" : lambda lx, lexical_entry: lexical_entry.set_lexeme(lx),
            "ps" : lambda ps, lexical_entry: lexical_entry.set_status(ps),
            "st" : lambda st, lexical_entry: lexical_entry.set_partOfSpeech(st)
        })
        # Read MDF file and test result
        lexicon = mdf_read(mdf_filename, mdf2lmf)
        entry = lexicon.lexical_entry[0]
        self.assertEqual(entry.get_lexeme(), "hello")
        self.assertEqual(entry.get_partOfSpeech(), "draft")
        self.assertEqual(entry.get_status(), "toto")
        del entry, lexicon
        # Remove MDF file
        os.remove(mdf_filename)

suite = unittest.TestLoader().loadTestsFromTestCase(TestMdfFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
