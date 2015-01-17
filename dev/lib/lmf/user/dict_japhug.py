#! /usr/bin/env python

## Needed to import LMF library properly
# Also automatically define 'user_path' as location of lib/lmf/user/ folder
from startup import *
import os

# Import user customized configuration
from japhug import mdf2lmf, lmf2mdf, order, lmf2tex

# Read MDF file and set lexicon identifier
lexical_resource = lmf.read_mdf(user_path + "../../../../dict/japhug/toolbox/Dictionary.txt", mdf2lmf, id="japhug")
# Set lexicon attributes
lexical_resource.get_lexicon("japhug").set_label("japhug online dictionary").set_language("jya").set_lexiconType("bilingual dictionary jya-fra")

# Set global information
lexical_resource.set_creationDate("2014-11-27")
lexical_resource.set_lastUpdate("2014-11-27")
lexical_resource.set_author("Guillaume Jacques")
lexical_resource.set_description("This is the japhug lexicon of HimalCo project.")
print lexical_resource.get_bibliographicCitation()

# Write XML LMF file
lmf.write_xml_lmf(lexical_resource, user_path + "dict_japhug/Dictionary.xml")

# Write LaTeX file
xml_order = lmf.read_sort_order(user_path + "config/japhug.xml")
lmf.write_tex(lexical_resource, user_path + "dict_japhug/Dictionary.tex", preamble=user_path + "config/japhug.tex", lmf2tex=lmf2tex, sort_order=xml_order)

# Write MDF file
lmf.write_mdf(lexical_resource, user_path + "dict_japhug/Dictionary.txt", lmf2mdf, order)

# Write HTML file
os.system("xsltproc -o " + user_path + "dict_japhug/Dictionary.html " + user_path + "../src/output/htm.xsl " + user_path + "dict_japhug/Dictionary.xml")

# Write document file
lmf.write_doc(lexical_resource, user_path + "dict_japhug/Dictionary.docx")

# Release created objects
del lexical_resource
