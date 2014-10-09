#! /usr/bin/env python

"""! @package input
"""

from config.mdf import mdf_lmf
from core.lexicon import Lexicon
from core.lexical_entry import LexicalEntry
from utils.io import open_read, EOL

def mdf_read(filename, mdf2lmf=mdf_lmf, id=None):
    """! @brief Read an MDF file.
    @param filename The name of the MDF file to read with full path, for instance 'user/input.txt'.
    @param mdf2lmf A Python dictionary describing the mapping between MDF markers and LMF representation. Default value is 'mdf_lmf' dictionary defined in 'src/config/mdf.py'. Please refer to it as an example.
    @param id A Python string identifying the created lexicon.
    @return A Lexicon instance containing all lexical entries.
    """
    import re
    mdf_file = open_read(filename)
    # MDF syntax is the following: '\marker value'
    mdf_pattern = """^\\\(\w*) (.*)$"""
    # Create a Lexicon instance to contain all lexical entries
    lexicon = Lexicon(id)
    # Add each lexical entry to the lexicon
    current_entry = None
    uid = 0
    for line in mdf_file.readlines():
        # Do not parse empty lines
        if line != EOL:
            result = re.match(mdf_pattern, line)
            marker = result.group(1)
            value = result.group(2)
            # 'lx' marker indicates a new entry
            if marker == "lx":
                # Create a new entry and add it to the lexicon
                uid += 1
                current_entry = LexicalEntry(uid)
                lexicon.add_lexical_entry(current_entry)
            # Map MDF marker and value to LMF representation
            mdf2lmf[marker](value, current_entry)
    mdf_file.close()
    # Verify lexicon coherence
    lexicon.check_cross_references()
    # Set lexicon attribute
    lexicon.set_entrySource(filename)
    return lexicon
