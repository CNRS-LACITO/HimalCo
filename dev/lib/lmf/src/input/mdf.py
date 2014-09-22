#! /usr/bin/env python

"""! @package input
"""

from config.mdf import mdf_lmf
from core.lexicon import Lexicon
from core.lexical_entry import LexicalEntry
from utils.io import open_read

def mdf_read(filename, mdf2lmf=mdf_lmf):
    """! @brief Read an MDF file.
    @param filename The name of the MDF file to read with full path, for instance 'user/input.txt'.
    @param mdf2lmf A Python dictionary describing the mapping between MDF markers and LMF representation. Default value is 'mdf_lmf' dictionary defined in 'src/config/mdf.py'. Please refer to it as an example.
    @return A Lexicon instance containing all lexical entries.
    """
    import re, os
    mdf_file = open_read(filename)
    # MDF syntax is the following: '\marker value'
    mdf_pattern = """^\\\(\w*) (.*)$"""
    # Create a Lexicon instance to contain all lexical entries
    lexicon = Lexicon()
    # Add each lexical entry to the lexicon
    current_entry = None
    if os.name == 'posix':
        # Linux-style end of line
        eol = '\n'
    else:
        # Windows-style end of line
        eol = '\r\n'
    for line in mdf_file.readlines():
        # Do not parse empty lines
        if line != eol:
            result = re.match(mdf_pattern, line)
            marker = result.group(1)
            value = result.group(2)
            # 'lx' marker indicates a new entry
            if marker == "lx":
                # Create a new entry and add it to the lexicon
                current_entry = LexicalEntry()
                lexicon.add_lexical_entry(current_entry)
            # Map MDF marker and value to LMF representation
            mdf2lmf[marker](value, current_entry)
    mdf_file.close()
    return lexicon
