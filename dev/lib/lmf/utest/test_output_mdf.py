#! /usr/bin/env python

from startup import *
from output.mdf import mdf_write
from core.lexicon import Lexicon
from core.lexical_entry import LexicalEntry
from morphology.lemma import Lemma

## Test MDF functions

class TestMdfFunctions(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_mdf_write(self):
        import sys, os
        # Create LMF objects
        lexical_entry = LexicalEntry()
        lexical_entry.lemma = Lemma()
        lexical_entry.partOfSpeech = "toto"
        lexical_entry.status = "draft"
        lexical_entry.lemma.lexeme = "hello"
        lexicon = Lexicon()
        lexicon.add_lexical_entry(lexical_entry)
        # Write MDF file and test result
        utest_path = sys.path[0] + '/'
        mdf_filename = utest_path + "output.txt"
        mdf_write(lexicon, mdf_filename)
        mdf_file = open(mdf_filename, "r")
        if os.name == 'posix':
            # Linux-style end of line
            eol = '\n'
        else:
            # Windows-style end of line
            eol = '\r\n'
        expected_lines = ["\\lx hello" + eol, "\\ps toto" + eol, "\\st draft" + eol, eol]
        self.assertListEqual(expected_lines, mdf_file.readlines())
        mdf_file.close()
        # Customize mapping
        lmf2mdf = dict({
            "lx" : lambda lexical_entry: lexical_entry.get_status(),
            "ps" : lambda lexical_entry: lexical_entry.get_partOfSpeech(),
            "st" : lambda lexical_entry: lexical_entry.get_lexeme()
        })
        order = ["st", "lx", "ps"]
        # Write MDF file and test result
        mdf_write(lexicon, mdf_filename, lmf2mdf, order)
        mdf_file = open(mdf_filename, "r")
        expected_lines = ["\\st hello" + eol, "\\lx draft" + eol, "\\ps toto" + eol, eol]
        self.assertListEqual(expected_lines, mdf_file.readlines())
        mdf_file.close()
        del lexical_entry.lemma, lexical_entry, lexicon
        # Remove MDF file
        os.remove(mdf_filename)

suite = unittest.TestLoader().loadTestsFromTestCase(TestMdfFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
