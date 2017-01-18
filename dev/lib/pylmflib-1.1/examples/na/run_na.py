#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Launch this script using the following command:
# ./examples/na/run_na.py

import sys, os, time

# Define 'user_path' as path location of pylmflib/examples/ folder
user_path = sys.path[0] + '/../'

# Add na configuration folder to path
sys.path.append(user_path + 'na')

# Add pylmflib/ folder to path
sys.path.append(user_path + '..')

# Create result folder
if not os.path.exists(user_path + "na/result"):
    os.mkdir(user_path + "na/result")

# Import LMF library
import pylmflib

# Import user customized configuration
# Les variables de type pylmflib.config.xml.TRUC correspondent à un attribut TRUC sous <Config><Language><lang> dans le fichier config.xml local !
from setting import tex_eng, tex_fra, tex_cmn, items, classify_lexicon

# Read user configuration
lexical_resource = pylmflib.read_config(user_path + "na/config.xml")

# Read MDF file, generate UID and set lexicon identifier
os.system("python2 " + user_path + "../pylmflib/utils/eol/eol.py -i " + user_path + "na/Dictionary.txt -o " + user_path + "na/result/dictionary-eol.txt")
os.system("python2 " + user_path + "../pylmflib/utils/uid/uid.py -i " + user_path + "na/result/dictionary-eol.txt -o " + user_path + "na/result/dictionary-uid.txt")
lexical_resource = pylmflib.read_mdf(id="na")

# Classify lexicon
(xml_order, xml_type) = pylmflib.read_sort_order(user_path + "na/sort_order.xml")
classify_lexicon(lexical_resource.get_lexicon("na"), xml_order, xml_type)

# Generate tables
os.system("python2 " + user_path + "../pylmflib/utils/tables/tables.py -i " + user_path + "na/Dictionary.txt -e " + user_path + "na/result/table_eng.tex -f " + user_path + "na/result/table_fra.tex -c" + user_path + "na/result/table_cmn.tex")

# Write LaTeX files: 
# anglais, français puis chinois
pylmflib.write_tex(lexical_resource, user_path + "na/result/dictionary_eng.tex", preamble=user_path + "na/preamble.tex", introduction=user_path + "na/introduction_eng.tex", lmf2tex=tex_eng, items=items, sort_order=xml_order, tables=[user_path + "na/result/table_eng.tex"], title=u"Na-English-Chinese-French Dictionary", tex_language="english", tex_other_languages=["chinese"])
pylmflib.write_tex(lexical_resource, user_path + "na/result/dictionary_fra.tex", preamble=user_path + "na/preamble.tex", introduction=user_path + "na/introduction_fra.tex", lmf2tex=tex_fra, items=items, sort_order=xml_order, tables=[user_path + "na/result/table_fra.tex"], title=u"Dictionnaire na-chinois-français", tex_language="french", tex_other_languages=["chinese"])
pylmflib.write_tex(lexical_resource, user_path + "na/result/dictionary_cmn.tex", preamble=user_path + "na/preamble.tex", introduction=user_path + "na/introduction_cmn.tex", lmf2tex=tex_cmn, items=items, sort_order=xml_order, tables=[user_path + "na/result/table_cmn.tex"], title=u"\zh{摩梭-汉-英-法词典}", tex_language="chinese", tex_other_languages=["english", "french"])

print("Nous compilons les fichiers Tex...")
# os.system("xelatex -output-directory=" + user_path + "na/result/ " + user_path + "na/result/dictionary_fra.tex --halt-on-error=N")
# os.system("xelatex -output-directory=" + user_path + "na/result/ " + user_path + "na/result/dictionary_fra.tex --halt-on-error=N")
# print(u"Nous avons compilé le français !")
# os.system("xelatex -output-directory=" + user_path + "na/result/ " + user_path + "na/result/dictionary_eng.tex --halt-on-error=N")
# os.system("xelatex -output-directory=" + user_path + "na/result/ " + user_path + "na/result/dictionary_eng.tex --halt-on-error=N")
# print(u"Nous avons compilé l'anglais !")
os.system("xelatex -output-directory=" + user_path + "na/result/ " + user_path + "na/result/dictionary_cmn.tex --halt-on-error=N")
os.system("xelatex -output-directory=" + user_path + "na/result/ " + user_path + "na/result/dictionary_cmn.tex --halt-on-error=N")
print(u"Nous avons compilé le chinois !")

# Write XML LMF file
pylmflib.write_xml_lmf(lexical_resource, user_path + "na/result/dictionary.xml")
# Release created objects
del lexical_resource
