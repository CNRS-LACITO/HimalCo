#! /usr/bin/env python

from startup import *
from output.tex import compute_header, tex_write
from core.lexical_resource import LexicalResource
from core.lexicon import Lexicon
from core.lexical_entry import LexicalEntry
from morphology.lemma import Lemma
from utils.io import EOL

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
        header = "\documentclass{article}" + EOL + "\\title{test}" + EOL + "\\author{C\'eline Buret}" + EOL
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
        lexical_resource = LexicalResource()
        lexical_resource.add_lexicon(lexicon)
        # Write LaTeX file and test result
        utest_path = sys.path[0] + '/'
        tex_filename = utest_path + "output.tex"
        tex_write(lexical_resource, tex_filename)
        tex_file = open(tex_filename, "r")
        begin_lines = [EOL,
            "\\begin{document}" + EOL,
            "\\maketitle" + EOL,
            "\\newpage" + EOL,
            "\\begin{multicols}{2}" + EOL
            ]
        end_lines = [
            "\end{multicols}" + EOL,
            "\end{document}" + EOL
            ]
        expected_lines = [EOL,
            "\\vspace{1cm} \\hspace{-1cm} {\Large \ipa{hello}} \\hspace{0.2cm} \\hypertarget{0}{}" + EOL,
            "\\textcolor{teal}{\\textit{toto}}" + EOL,
            EOL]
        self.assertListEqual(begin_lines + expected_lines + end_lines, tex_file.readlines())
        tex_file.close()
        # Customize mapping
        lmf2tex = dict({
            "Lemma.lexeme" : lambda lexical_entry: "is " + lexical_entry.get_lexeme() + "." + EOL,
            "LexicalEntry.id" : lambda lexical_entry: EOL + "The lexical entry " + str(lexical_entry.get_id()) + " ",
            "LexicalEntry.partOfSpeech" : lambda lexical_entry: "Its grammatical category is " + lexical_entry.get_partOfSpeech() + "." + EOL,
            "LexicalEntry.status" : lambda lexical_entry: "Warning: " + lexical_entry.get_status() + " version!" + EOL
        })
        order = ["LexicalEntry.id", "Lemma.lexeme", "LexicalEntry.partOfSpeech", "LexicalEntry.status"]
        # Write LaTeX file and test result
        tex_write(lexical_resource, tex_filename, None, lmf2tex, order)
        tex_file = open(tex_filename, "r")
        expected_lines = [EOL,
            "The lexical entry 0 is hello." + EOL,
            "Its grammatical category is toto." + EOL,
            "Warning: draft version!" + EOL,
            EOL]
        self.assertListEqual(begin_lines + expected_lines + end_lines, tex_file.readlines())
        tex_file.close()
        del lexical_entry.lemma
        lexical_entry.lemma = None
        del lexical_entry, lexicon
        lexicon = None
        del lexical_resource
        # Remove LaTeX file
        os.remove(tex_filename)

suite = unittest.TestLoader().loadTestsFromTestCase(TestTexFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
