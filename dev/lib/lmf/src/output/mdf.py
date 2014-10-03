#! /usr/bin/env python

from config.mdf import lmf_mdf, mdf_order
from utils.io import open_write, EOL

def mdf_write(object, filename, lmf2mdf=lmf_mdf, order=mdf_order):
    """! @brief Write an MDF file.
    @param object The LMF instance to convert into MDF output format.
    @param filename The name of the MDF file to write with full path, for instance 'user/output.txt'.
    @param lmf2mdf A Python dictionary describing the mapping between LMF representation and MDF markers. Default value is 'lmf_mdf' dictionary defined in 'src/config/mdf.py'. Please refer to it as an example.
    @param order A Python list defining the order in which MDf markers must be written, for instance ["lx", "ps"]. Default value is 'mdf_order' list defined in 'src/config/mdf.py'.
    """
    mdf_file = open_write(filename)
    # For each MDF marker, get the corresponding LMF value
    if object.__class__.__name__ == "Lexicon":
        for lexical_entry in object.get_lexical_entries():
            for marker in order:
                value = lmf2mdf[marker](lexical_entry)
                if type(value) is not list:
                    # Write the MDF output as follows: "\mdf_marker lmf_value"
                    mdf_file.write("\\" + marker + " " + value + EOL)
                else:
                    # Create a line for each value
                    for item in value:
                        mdf_file.write("\\" + marker + " " + item + EOL)
            # Separate lexical entries from each others with a blank line
            mdf_file.write(EOL)
    else:
        raise AttributeError(0, __file__, "Object to write must be a Lexicon.")
    mdf_file.close()
