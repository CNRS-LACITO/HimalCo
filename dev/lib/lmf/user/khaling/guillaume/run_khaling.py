#! /usr/bin/env python

# Go under dev/lib/lmf/ and launch this script using the following command:
# ./user/khaling/guillaume/run_khaling.py

import sys, os

# Define 'user_path' as path location of lib/lmf/user/ folder
user_path = sys.path[0] + '/../../'

# Add khaling configuration folder to path
sys.path.append(user_path + 'khaling')

# Add lib/ folder to path
sys.path.append(user_path + '../..')

# Import LMF library
import lmf

# Import user customized configuration
from setting import lmf2tex, items

# Read user configuration
lexical_resource = lmf.read_config(user_path + "khaling/guillaume/config.xml")

# Run Perl script
os.system("perl " + user_path + "../src/utils/ipa2devanagari/ipa2devanagari.pl " + user_path + "../../../../dict/khaling/toolbox/Dictionary.txt " + user_path + "khaling/result/dictionary-dev.txt")

# Read MDF file and set lexicon identifier
lexical_resource = lmf.read_mdf(id="khaling")

# Classify lexicon
sort_order = lambda character: ord(character.encode('utf-8').decode('utf-8'))
lexical_resource.get_lexicon("khaling").sort_lexical_entries(items=items, sort_order=sort_order)

# Generate paradigms
os.system("rm " + user_path + "khaling/result/paradigms.tex")
os.system("perl " + user_path + "../src/utils/paradigms/paradigms.pl " + user_path + "khaling/verbs.txt " + user_path + "khaling/result/paradigms.tex")

# Write LaTeX file
lmf.write_tex(lexical_resource, user_path + "khaling/result/dictionary.tex", preamble=user_path + "khaling/guillaume/khaling.tex", lmf2tex=lmf2tex, items=items, sort_order=sort_order, paradigms=user_path + "khaling/result/paradigms.tex")

# Release created objects
del lexical_resource
