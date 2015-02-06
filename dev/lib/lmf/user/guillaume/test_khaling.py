#! /usr/bin/env python

import sys, os

# Define 'user_path' as path location of lib/lmf/user/ folder
user_path = sys.path[0] + '/../'

# Add user configuration folder to path
sys.path.append(user_path + 'config')

# Add lib/ folder to path
sys.path.append(user_path + '../..')

# Import LMF library
import lmf

# Import user customized configuration
from khaling import mdf2lmf, lmf2mdf, order, lmf2tex, items, my_font

# Run Perl script
os.system("perl " + user_path + "../src/utils/ipa2devanagari/ipa2devanagari.pl " + user_path + "guillaume/test_input.txt " + user_path + "guillaume/test_output.txt")

# Read MDF file and set lexicon identifier
lexical_resource = lmf.read_mdf(user_path + "guillaume/test_output.txt", mdf2lmf, id="khaling")

# Classify lexicon
sort_order = lambda character: ord(character.encode('utf-8').decode('utf-8'))
lexical_resource.get_lexicon("khaling").sort_lexical_entries(items=items, sort_order=sort_order)

# Write LaTeX file
lmf.write_tex(lexical_resource, user_path + "guillaume/test.tex", preamble=user_path + "config/khaling.tex", lmf2tex=lmf2tex, font=my_font, items=items, sort_order=sort_order)

# Release created objects
del lexical_resource
