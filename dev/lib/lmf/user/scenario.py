#! /usr/bin/env python

import startup, sys
from src import *

from na import mdf2lmf

user_path = sys.path[0] + '/'

# Read MDF file
input = mdf_read(user_path + "input.txt", mdf2lmf)

# Write XML LMF file
lmf_write(input, user_path + "output.xml")

# Read XML LMF file
output = lmf_read(user_path + "output.xml")

# Write LaTeX file
tex_write(output, user_path + "output.tex", preamble=user_path + "config/japhug.tex")

# Write MDF file
mdf_write(output, user_path + "output.txt")
