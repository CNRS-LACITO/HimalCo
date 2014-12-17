#! /usr/bin/env python

## Needed to import LMF library properly
# Also automatically define 'user_path' as location of lib/lmf/user/ folder
from startup import *
import os

# Import user customized configuration
import japhug, khaling, koyi, na, thulung

# Read MDF files and set lexicons identifiers
japhug_lexical_resource = lmf.read_mdf(user_path + "demo/japhug_input.txt", japhug.mdf2lmf, id="japhug")
khaling_lexical_resource = lmf.read_mdf(user_path + "demo/khaling_input.txt", khaling.mdf2lmf, id="khaling")
koyi_lexical_resource = lmf.read_mdf(user_path + "demo/koyi_input.txt", koyi.mdf2lmf, id="koyi")
na_lexical_resource = lmf.read_mdf(user_path + "demo/na_input.txt", na.mdf2lmf, id="na")
thulung_lexical_resource = lmf.read_mdf(user_path + "demo/thulung_input.txt", thulung.mdf2lmf, id="thulung")

# Set lexicons attributes
japhug_lexical_resource.get_lexicon("japhug").set_label("japhug online dictionary").set_language("jya").set_lexiconType("bilingual dictionary jya-fra")
khaling_lexical_resource.get_lexicon("khaling").set_label("khaling online dictionary").set_language("klr").set_lexiconType("bilingual dictionary klr-eng")
koyi_lexical_resource.get_lexicon("koyi").set_label("koyi online dictionary").set_language("kkt").set_lexiconType("bilingual dictionary kkt-eng")
na_lexical_resource.get_lexicon("na").set_label("na online dictionary").set_language("nru").set_lexiconType("trilingual dictionary nru-eng-fra")
thulung_lexical_resource.get_lexicon("thulung").set_label("thulung online dictionary").set_language("tdh").set_lexiconType("bilingual dictionary tdh-eng")

# Write XML LMF files
lmf.write_xml_lmf(japhug_lexical_resource, user_path + "demo/japhug_output.xml")
lmf.write_xml_lmf(khaling_lexical_resource, user_path + "demo/khaling_output.xml")
lmf.write_xml_lmf(koyi_lexical_resource, user_path + "demo/koyi_output.xml")
lmf.write_xml_lmf(na_lexical_resource, user_path + "demo/na_output.xml")
lmf.write_xml_lmf(thulung_lexical_resource, user_path + "demo/thulung_output.xml")

# Write LaTeX files
lmf.write_tex(japhug_lexical_resource, user_path + "demo/japhug_output.tex", preamble=user_path + "config/japhug.tex", lmf2tex=japhug.lmf2tex, sort_order=japhug.ranks)
lmf.write_tex(khaling_lexical_resource, user_path + "demo/khaling_output.tex", preamble=user_path + "config/khaling.tex")
lmf.write_tex(koyi_lexical_resource, user_path + "demo/koyi_output.tex", preamble=user_path + "config/koyi.tex")
lmf.write_tex(na_lexical_resource, user_path + "demo/na_output_eng.tex", preamble=user_path + "config/na.tex", lmf2tex=na.tex_eng)
lmf.write_tex(na_lexical_resource, user_path + "demo/na_output_fra.tex", preamble=user_path + "config/na.tex", lmf2tex=na.tex_fra)
lmf.write_tex(thulung_lexical_resource, user_path + "demo/thulung_output.tex", preamble=user_path + "config/thulung.tex")

# Write MDF files
lmf.write_mdf(japhug_lexical_resource, user_path + "demo/japhug_output.txt", japhug.lmf2mdf, japhug.order)
lmf.write_mdf(khaling_lexical_resource, user_path + "demo/khaling_output.txt", khaling.lmf2mdf, khaling.order)
lmf.write_mdf(koyi_lexical_resource, user_path + "demo/koyi_output.txt", koyi.lmf2mdf, koyi.order)
lmf.write_mdf(na_lexical_resource, user_path + "demo/na_output.txt", na.lmf2mdf, na.order)
lmf.write_mdf(thulung_lexical_resource, user_path + "demo/thulung_output.txt", thulung.lmf2mdf, thulung.order)

# Write HTML files
os.system("xsltproc -o " + user_path + "demo/japhug_output.html " + user_path + "../src/output/htm.xsl " + user_path + "demo/japhug_output.xml")
os.system("xsltproc -o " + user_path + "demo/khaling_output.html " + user_path + "../src/output/htm.xsl " + user_path + "demo/khaling_output.xml")
os.system("xsltproc -o " + user_path + "demo/koyi_output.html " + user_path + "../src/output/htm.xsl " + user_path + "demo/koyi_output.xml")
os.system("xsltproc -o " + user_path + "demo/na_output.html " + user_path + "../src/output/htm.xsl " + user_path + "demo/na_output.xml")
os.system("xsltproc -o " + user_path + "demo/thulung_output.html " + user_path + "../src/output/htm.xsl " + user_path + "demo/thulung_output.xml")

# Write document files
lmf.write_doc(japhug_lexical_resource, user_path + "demo/japhug_output.docx")
lmf.write_doc(khaling_lexical_resource, user_path + "demo/khaling_output.docx")
lmf.write_doc(koyi_lexical_resource, user_path + "demo/koyi_output.docx")
lmf.write_doc(na_lexical_resource, user_path + "demo/na_output.docx")
lmf.write_doc(thulung_lexical_resource, user_path + "demo/thulung_output.docx")

# Release created objects
del japhug_lexical_resource, khaling_lexical_resource, koyi_lexical_resource, na_lexical_resource, thulung_lexical_resource
