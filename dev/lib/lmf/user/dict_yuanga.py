#! /usr/bin/env python

## Needed to import LMF library properly
# Also automatically define 'user_path' as location of lib/lmf/user/ folder
from startup import *
import os

# Add user yuanga folder to path
sys.path.append(user_path + 'yuanga')

# Import user customized configuration
from setting import lmf2tex, items

# Read user configuration
lexical_resource = lmf.read_config(user_path + "yuanga/config.xml")

# Read MDF file and set lexicon identifier
lexical_resource = lmf.read_mdf(id="yuanga", encoding='latin-1')

# Display global information
print lexical_resource.get_bibliographic_citation()

# Classify lexicon
xml_order = lmf.read_sort_order(user_path + "yuanga/sort_order.xml")
lexical_resource.get_lexicon("yuanga").sort_lexical_entries(items=items, sort_order=xml_order)

# Write XML LMF file
lmf.write_xml_lmf(lexical_resource, user_path + "yuanga/result/yuanga.xml")

# Write LaTeX file
lmf.write_tex(lexical_resource, user_path + "yuanga/result/yuanga.tex", preamble=user_path + "yuanga/yuanga.tex", lmf2tex=lmf2tex, items=items, sort_order=xml_order)

# Write MDF file
lmf.write_mdf(lexical_resource, user_path + "yuanga/result/yuanga.txt")

# Write HTML file
os.system("xsltproc -o " + user_path + "yuanga/result/yuanga.html " + user_path + "../src/output/htm.xsl " + user_path + "yuanga/result/yuanga.xml")

# Write document file
lmf.write_doc(lexical_resource, user_path + "yuanga/result/yuanga.docx")

# Release created objects
del lexical_resource
