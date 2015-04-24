#! /usr/bin/env python

## Needed to import LMF library properly
# Also automatically define 'user_path' as location of lib/lmf/user/ folder
from startup import *
import os

# Add japhug configuration folder to path
sys.path.append(user_path + 'japhug')

# Create result folder
if not os.path.exists(user_path + "japhug/result"):
    os.mkdir(user_path + "japhug/result")

# Import user customized configuration
from setting import lmf2tex, items

# Read user configuration
lexical_resource = lmf.read_config(user_path + "japhug/config.xml")

# Read MDF file and set lexicon identifier
lexical_resource = lmf.read_mdf(id="japhug")

# Display global information
print lexical_resource.get_bibliographic_citation()

# Classify lexicon
xml_order = lmf.read_sort_order(user_path + "japhug/sort_order.xml")
lexical_resource.get_lexicon("japhug").sort_lexical_entries(items=items, sort_order=xml_order)

# Write XML LMF file
lmf.write_xml_lmf(lexical_resource, user_path + "japhug/result/dictionary.xml")

# Write LaTeX file
lmf.write_tex(lexical_resource, user_path + "japhug/result/dictionary.tex", preamble=user_path + "japhug/japhug.tex", lmf2tex=lmf2tex, items=items, sort_order=xml_order)

# Write MDF file
lmf.write_mdf(lexical_resource, user_path + "japhug/result/dictionary.txt")

# Write HTML file
os.system("xsltproc -o " + user_path + "japhug/result/dictionary.html " + user_path + "../src/output/htm.xsl " + user_path + "japhug/result/dictionary.xml")

# Write document file
lmf.write_doc(lexical_resource, user_path + "japhug/result/dictionary.docx")

# Release created objects
del lexical_resource
