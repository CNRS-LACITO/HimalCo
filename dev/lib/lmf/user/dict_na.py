#! /usr/bin/env python

## Needed to import LMF library properly
# Also automatically define 'user_path' as location of lib/lmf/user/ folder
from startup import *
import os

# Import user customized configuration
from na import mdf2lmf, lmf2mdf, order, tex_eng, tex_fra

# Read MDF file and set lexicon identifier
lexical_resource = lmf.read_mdf(user_path + "../../../../dict/na/toolbox/Dictionary.txt", mdf2lmf, id="na")
# Set lexicon attributes
lexical_resource.get_lexicon("na").set_label("na online dictionary").set_language("nru").set_lexiconType("trilingual dictionary nru-eng-fra")

# Set global information
lexical_resource.set_creationDate("2015-02-20")
lexical_resource.set_lastUpdate("2015-02-20")
lexical_resource.set_author("Alexis Michaud")
lexical_resource.set_description("This is the na lexicon of HimalCo project.")
print lexical_resource.get_bibliographicCitation()

# Classify lexicon
xml_order = lmf.read_sort_order(user_path + "config/na.xml")
lexical_resource.get_lexicon("na").sort_lexical_entries(sort_order=xml_order)

# Write XML LMF file
lmf.write_xml_lmf(lexical_resource, user_path + "dict_na/Dictionary.xml")

# Write LaTeX file
lmf.write_tex(lexical_resource, user_path + "dict_na/Dictionary_eng.tex", preamble=user_path + "config/na.tex", lmf2tex=tex_eng, sort_order=xml_order)
lmf.write_tex(lexical_resource, user_path + "dict_na/Dictionary_fra.tex", preamble=user_path + "config/na.tex", lmf2tex=tex_fra, sort_order=xml_order)

# Write MDF file
lmf.write_mdf(lexical_resource, user_path + "dict_na/Dictionary.txt", lmf2mdf, order)

# Release created objects
del lexical_resource
