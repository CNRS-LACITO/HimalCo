#! /usr/bin/env python

## User functions to read from a file: MDF, XML LMF
from input.mdf import mdf_read
from input.xml_lmf import xml_lmf_read as lmf_read

## User functions to write into a file: MDF, XML LMF, LaTeX
from output.mdf import mdf_write
from output.xml_lmf import xml_lmf_write as lmf_write
from output.tex import tex_write
