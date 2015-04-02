#! /usr/bin/env python

# Go under dev/lib/lmf/ and launch this script using the following command:
# ./user/japhug/guillaume/run_japhug.py

import sys, os

# Define 'user_path' as path location of lib/lmf/user/ folder
user_path = sys.path[0] + '/../../'

# Add japhug configuration folder to path
sys.path.append(user_path + 'japhug')

# Add lib/ folder to path
sys.path.append(user_path + '../..')

# Create result folder
if not os.path.exists(user_path + "japhug/result"):
    os.mkdir(user_path + "japhug/result")

# Import LMF library
import lmf

# Import user customized configuration
from setting import lmf2tex

# Read user configuration
lexical_resource = lmf.read_config(user_path + "japhug/config.xml")

# Read MDF file and set lexicon identifier
lexical_resource = lmf.read_mdf(id="japhug")

# Classify lexicon
xml_order = lmf.read_sort_order(user_path + "japhug/sort_order.xml")
lexical_resource.get_lexicon("japhug").sort_lexical_entries(sort_order=xml_order)

# Write LaTeX file
lmf.write_tex(lexical_resource, user_path + "japhug/result/dictionary.tex", preamble=user_path + "japhug/japhug.tex", lmf2tex=lmf2tex, sort_order=xml_order)

# Release created objects
del lexical_resource
