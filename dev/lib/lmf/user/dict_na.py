#! /usr/bin/env python

## Needed to import LMF library properly
# Also automatically define 'user_path' as location of lib/lmf/user/ folder
from startup import *
import os

# Add na configuration folder to path
sys.path.append(user_path + 'na')

# Import user customized configuration
from setting import mdf2lmf, lmf2mdf, order, tex_eng, tex_fra

# Read user configuration
lexical_resource = lmf.read_config(user_path + "na/config.xml")

# Read MDF file and set lexicon identifier
lexical_resource = lmf.read_mdf(mdf2lmf=mdf2lmf, id="na")

# Display global information
print lexical_resource.get_bibliographic_citation()

# Classify lexicon
xml_order = lmf.read_sort_order(user_path + "na/sort_order.xml")
lexical_resource.get_lexicon("na").sort_lexical_entries(sort_order=xml_order)

# Write XML LMF file
lmf.write_xml_lmf(lexical_resource, user_path + "na/result/dictionary.xml")

# Write LaTeX file
lmf.write_tex(lexical_resource, user_path + "na/result/dictionary_eng.tex", preamble=user_path + "na/na.tex", lmf2tex=tex_eng, sort_order=xml_order)
lmf.write_tex(lexical_resource, user_path + "na/result/dictionary_fra.tex", preamble=user_path + "na/na.tex", lmf2tex=tex_fra, sort_order=xml_order)

# Write MDF file
lmf.write_mdf(lexical_resource, user_path + "na/result/dictionary.txt", lmf2mdf, order)

# Release created objects
del lexical_resource
