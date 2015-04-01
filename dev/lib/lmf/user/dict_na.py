#! /usr/bin/env python

## Needed to import LMF library properly
# Also automatically define 'user_path' as location of lib/lmf/user/ folder
from startup import *
import os

# Add na configuration folder to path
sys.path.append(user_path + 'na')

# Create result folder
if not os.path.exists(user_path + "na/result"):
    os.mkdir(user_path + "na/result")

# Import user customized configuration
from setting import tex_eng, tex_fra, items

# Read user configuration
lexical_resource = lmf.read_config(user_path + "na/config.xml")

# Read MDF file and set lexicon identifier
os.system("python " + user_path + "../src/utils/eol/eol.py -i " + user_path + "../../../../dict/na/toolbox/Dictionary.txt -o " + user_path + "na/result/dictionary-eol.txt")
lexical_resource = lmf.read_mdf(id="na")

# Display global information
print lexical_resource.get_bibliographic_citation()

# Classify lexicon
xml_order = lmf.read_sort_order(user_path + "na/sort_order.xml")
lexical_resource.get_lexicon("na").sort_lexical_entries(items=items, sort_order=xml_order)

# Write XML LMF file
lmf.write_xml_lmf(lexical_resource, user_path + "na/result/dictionary.xml")

# Write LaTeX files
lmf.write_tex(lexical_resource, user_path + "na/result/dictionary_eng.tex", preamble=user_path + "na/na.tex", lmf2tex=tex_eng, items=items, sort_order=xml_order)
lmf.write_tex(lexical_resource, user_path + "na/result/dictionary_fra.tex", preamble=user_path + "na/na.tex", lmf2tex=tex_fra, items=items, sort_order=xml_order)

# Write MDF file
lmf.write_mdf(lexical_resource, user_path + "na/result/dictionary.txt")

# Release created objects
del lexical_resource
