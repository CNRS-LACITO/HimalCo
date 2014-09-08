#! /usr/bin/env python

from startup import *
from output.tex import compute_header, tex_write
from core.lexicon import Lexicon
from core.lexical_entry import LexicalEntry
from morphology.lemma import Lemma

## Test LaTeX functions

class TestTexFunctions(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_compute_header(self):
        import sys, os
        # Create a header LaTeX file
        utest_path = sys.path[0] + '/'
        tex_filename = utest_path + "header.tex"
        tex_file = open(tex_filename, "w+")
        header = "\documentclass{article}\n\\title{test}\n\\author{C\'eline Buret}\n"
        tex_file.write(header)
        tex_file.close()
        # Read header file and test result
        self.assertEqual(compute_header(tex_filename), header)
        # Remove LaTeX file
        os.remove(tex_filename)

    def test_tex_write(self):
        import sys, os
        # Create LMF objects
        lexical_entry = LexicalEntry()
        lexical_entry.lemma = Lemma()
        lexical_entry.partOfSpeech = "toto"
        lexical_entry.status = "draft"
        lexical_entry.lemma.lexeme = "hello"
        lexicon = Lexicon()
        lexicon.add_lexical_entry(lexical_entry)
        # Write LaTeX file and test result
        utest_path = sys.path[0] + '/'
        tex_filename = utest_path + "output.tex"
        tex_write(lexicon, tex_filename)
        tex_file = open(tex_filename, "r")
        begin_lines = ["\n",
            "\\begin{document}\n",
            "\\maketitle\n",
            "\\newpage\n",
            "\\begin{multicols}{2}\n"
            ]
        end_lines = [
            "\end{multicols}\n",
            "\end{document}\n"
            ]
        expected_lines = ["\n",
            "\\vspace{1cm} \\hspace{-1cm} {\Large \ipa{hello}} \\hspace{0.2cm} \\hypertarget{0}{}\n",
            "\\textcolor{teal}{\\textit{toto}}\n",
            "\n"]
        self.assertListEqual(begin_lines + expected_lines + end_lines, tex_file.readlines())
        tex_file.close()
        # Customize mapping
        lmf2tex = dict({
            "Lemma.lexeme" : lambda lexical_entry: "is " + lexical_entry.get_lexeme() + ".\n",
            "LexicalEntry.id" : lambda lexical_entry: "\nThe lexical entry " + str(lexical_entry.get_id()) + " ",
            "LexicalEntry.partOfSpeech" : lambda lexical_entry: "Its grammatical category is " + lexical_entry.get_partOfSpeech() + ".\n",
            "LexicalEntry.status" : lambda lexical_entry: "Warning: " + lexical_entry.get_status() + " version!\n"
        })
        order = ["LexicalEntry.id", "Lemma.lexeme", "LexicalEntry.partOfSpeech", "LexicalEntry.status"]
        # Write LaTeX file and test result
        tex_write(lexicon, tex_filename, None, lmf2tex, order)
        tex_file = open(tex_filename, "r")
        expected_lines = ["\n",
            "The lexical entry 0 is hello.\n",
            "Its grammatical category is toto.\n",
            "Warning: draft version!\n",
            "\n"]
        self.assertListEqual(begin_lines + expected_lines + end_lines, tex_file.readlines())
        tex_file.close()
        del lexical_entry.lemma, lexical_entry, lexicon
        # Remove LaTeX file
        os.remove(tex_filename)

suite = unittest.TestLoader().loadTestsFromTestCase(TestTexFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
