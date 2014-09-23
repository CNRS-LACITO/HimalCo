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
        if os.name == 'posix':
            # Unix-style end of line
            eol = '\n'
        else:
            # Windows-style end of line
            eol = '\r\n'
        header = "\documentclass{article}" + eol + "\\title{test}" + eol + "\\author{C\'eline Buret}" + eol
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
        if os.name == 'posix':
            # Unix-style end of line
            eol = '\n'
        else:
            # Windows-style end of line
            eol = '\r\n'
        begin_lines = [eol,
            "\\begin{document}" + eol,
            "\\maketitle" + eol,
            "\\newpage" + eol,
            "\\begin{multicols}{2}" + eol
            ]
        end_lines = [
            "\end{multicols}" + eol,
            "\end{document}" + eol
            ]
        expected_lines = [eol,
            "\\vspace{1cm} \\hspace{-1cm} {\Large \ipa{hello}} \\hspace{0.2cm} \\hypertarget{0}{}" + eol,
            "\\textcolor{teal}{\\textit{toto}}" + eol,
            eol]
        self.assertListEqual(begin_lines + expected_lines + end_lines, tex_file.readlines())
        tex_file.close()
        # Customize mapping
        lmf2tex = dict({
            "Lemma.lexeme" : lambda lexical_entry: "is " + lexical_entry.get_lexeme() + "." + eol,
            "LexicalEntry.id" : lambda lexical_entry: eol + "The lexical entry " + str(lexical_entry.get_id()) + " ",
            "LexicalEntry.partOfSpeech" : lambda lexical_entry: "Its grammatical category is " + lexical_entry.get_partOfSpeech() + "." + eol,
            "LexicalEntry.status" : lambda lexical_entry: "Warning: " + lexical_entry.get_status() + " version!" + eol
        })
        order = ["LexicalEntry.id", "Lemma.lexeme", "LexicalEntry.partOfSpeech", "LexicalEntry.status"]
        # Write LaTeX file and test result
        tex_write(lexicon, tex_filename, None, lmf2tex, order)
        tex_file = open(tex_filename, "r")
        expected_lines = [eol,
            "The lexical entry 0 is hello." + eol,
            "Its grammatical category is toto." + eol,
            "Warning: draft version!" + eol,
            eol]
        self.assertListEqual(begin_lines + expected_lines + end_lines, tex_file.readlines())
        tex_file.close()
        del lexical_entry.lemma, lexical_entry, lexicon
        # Remove LaTeX file
        os.remove(tex_filename)

suite = unittest.TestLoader().loadTestsFromTestCase(TestTexFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
