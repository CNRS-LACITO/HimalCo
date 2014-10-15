#! /usr/bin/env python

## Needed to import LMF library properly
# Also automatically define 'user_path' as location of lib/lmf/user/ folder
from startup import *

# Import user customized configuration if any
from na import mdf2lmf

# Read MDF file and set lexicon identifier
input_lexical_resource = lmf.read_mdf(user_path + "input.txt", mdf2lmf, id="short example")
# Set lexicon attributes
input_lexical_resource.get_lexicon("short example").set_label("test online dictionary").set_language("eng").set_languageScript("latn").set_lexiconType("bilingual dictionary na-eng")

# Set global information
input_lexical_resource.set_creationDate("2014-10-01")
input_lexical_resource.set_lastUpdate("2014-10-10")
input_lexical_resource.set_author("Celine Buret")
input_lexical_resource.set_description("This is a testing lexicon.")
print input_lexical_resource.get_bibliographicCitation()

# Write XML LMF file
lmf.write_xml_lmf(input_lexical_resource, user_path + "output.xml")

# Read XML LMF file
output_lexical_resource = lmf.read_xml_lmf(user_path + "output.xml")

# Write LaTeX file
lmf.write_tex(output_lexical_resource, user_path + "output.tex", preamble=user_path + "config/japhug.tex")

# Write MDF file
lmf.write_mdf(output_lexical_resource, user_path + "output.txt")

# Release created objects
del input_lexical_resource, output_lexical_resource
