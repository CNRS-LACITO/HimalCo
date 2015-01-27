#! /usr/bin/env python
# -*- coding: utf-8 -*-

## Needed to import LMF library properly
# Also automatically define 'ftest_path' as location of lib/lmf/ftest/ folder
from startup import *
import os

# Read MDF file and set lexicon identifier
input_lexical_resource = lmf.read_mdf(ftest_path + "input.txt", id="short example")

# Set global information
input_lexical_resource.set_creationDate("2014-10-01")
input_lexical_resource.set_lastUpdate("2014-10-10")
input_lexical_resource.set_author(u"Céline Buret")
input_lexical_resource.set_description("This is a testing lexicon.")
print input_lexical_resource.get_bibliographicCitation()

# Get created lexicon
my_lexicon = input_lexical_resource.get_lexicon("short example")

# Set lexicon attributes
my_lexicon.set_label("test online dictionary").set_language("eng").set_languageScript("latn").set_lexiconType("bilingual dictionary")

# Alphabetize lexemes
my_lexicon.sort_lexical_entries()

# Write XML LMF file
lmf.write_xml_lmf(input_lexical_resource, ftest_path + "output.xml")

# Read XML LMF file
output_lexical_resource = lmf.read_xml_lmf(ftest_path + "output.xml")

# Write LaTeX file
lmf.write_tex(output_lexical_resource, ftest_path + "output.tex", preamble=ftest_path + "header.tex")

# Write MDF file
lmf.write_mdf(output_lexical_resource, ftest_path + "output.txt")

# Write HTML file
os.system("xsltproc -o " + ftest_path + "output.html " + ftest_path + "../src/output/htm.xsl " + ftest_path + "output.xml")

# Write document file
lmf.write_doc(output_lexical_resource, ftest_path + "output.docx")

# Release created objects
del input_lexical_resource, output_lexical_resource
