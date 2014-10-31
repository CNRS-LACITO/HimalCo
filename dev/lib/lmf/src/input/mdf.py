#! /usr/bin/env python

"""! @package input
"""

from config.mdf import mdf_lmf
from core.lexicon import Lexicon
from core.lexical_entry import LexicalEntry
from utils.io import open_read, EOL
from utils.error_handling import Warning, Error

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
    mdf_pattern = """^\\\(\w*) (<(.*)>)? ?(.*)$"""
    # Create a Lexicon instance to contain all lexical entries
    lexicon = Lexicon(id)
    # Add each lexical entry to the lexicon
    current_entry = None
    for line in mdf_file.readlines():
        # Do not parse empty lines
        if line != EOL:
            result = re.match(mdf_pattern, line)
            marker = result.group(1)
            attrs = result.group(3)
            value = result.group(4)
            # Do not consider empty fields
            if value == "":
                continue
            # 'lx' marker indicates a new entry
            if marker == "lx":
                # Compute a unique identifier
                occurrence_nb = 1
                # Python equivalent of do...while loop
                while True:
                    uid = value + "_" + str(occurrence_nb)
                    # If already taken, increment it
                    if lexicon.find_lexical_entries(lambda lexical_entry: lexical_entry.get_id() == uid) != []:
                        occurrence_nb += 1
                    else:
                        # Create a new entry
                        current_entry = LexicalEntry(uid)
                        break
                # Add it to the lexicon
                lexicon.add_lexical_entry(current_entry)
            # Map MDF marker and value to LMF representation
            try:
                if attrs is not None:
                    # There are attributes
                    attributes = {}
                    # Remove quotation marks from attributes if any
                    attrs = attrs.replace('"', '')
                    for attr in attrs.split(' '):
                        attributes.update({attr.split('=')[0] : attr.split('=')[1]})
                    # A customized marker starts with '__' characters
                    mdf2lmf["__" + marker](attributes, value, current_entry)
                else:
                    mdf2lmf[marker](value, current_entry)
            except KeyError:
                print Warning("MDF marker '%s' encountered for lexeme '%s' is not defined in configuration" % (marker, current_entry.get_lexeme()))
            except Error as exception:
                exception.handle()
    mdf_file.close()
    # Verify lexicon coherence
    lexicon.check_cross_references()
    # Set lexicon attribute
    lexicon.set_entrySource(filename)
    return lexicon
