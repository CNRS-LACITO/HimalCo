#! /usr/bin/env python

## Needed to import LMF library properly
# Also automatically define 'user_path' as location of lib/lmf/user/ folder
from startup import *
import os

# Import user customized configuration
from khaling import mdf2lmf, lmf2mdf, order, lmf2tex, unicode_ranks, items

# Read MDF file and set lexicon identifier
lexical_resource = lmf.read_mdf(user_path + "../../../../dict/khaling/toolbox/Dictionary.txt", mdf2lmf, id="khaling")
# Set lexicon attributes
lexical_resource.get_lexicon("khaling").set_label("khaling online dictionary").set_language("klr").set_lexiconType("bilingual dictionary klr-fra")

# Set global information
lexical_resource.set_creationDate("2015-01-16")
lexical_resource.set_lastUpdate("2015-01-16")
lexical_resource.set_author("Guillaume Jacques")
lexical_resource.set_description("This is the khaling lexicon of HimalCo project.")
print lexical_resource.get_bibliographicCitation()

# Write XML LMF file
lmf.write_xml_lmf(lexical_resource, user_path + "dict_khaling/Dictionary.xml")

# Write LaTeX file
lmf.write_tex(lexical_resource, user_path + "dict_khaling/Dictionary.tex", preamble=user_path + "config/khaling.tex", lmf2tex=lmf2tex, sort_order=unicode_ranks)
lmf.write_tex(lexical_resource, user_path + "dict_khaling/Dictionary-ge.tex", preamble=user_path + "config/khaling.tex", lmf2tex=lmf2tex, items=items)

# Write MDF file
lmf.write_mdf(lexical_resource, user_path + "dict_khaling/Dictionary.txt", lmf2mdf, order)

# Write HTML file
os.system("xsltproc -o " + user_path + "dict_khaling/Dictionary.html " + user_path + "../src/output/htm.xsl " + user_path + "dict_khaling/Dictionary.xml")

# Write document file
lmf.write_doc(lexical_resource, user_path + "dict_khaling/Dictionary.docx")

# Release created objects
del lexical_resource
