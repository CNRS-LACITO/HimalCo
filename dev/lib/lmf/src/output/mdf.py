#! /usr/bin/env python

from config.mdf import lmf_mdf, mdf_order
from utils.io import open_write, EOL
from utils.error_handling import OutputError

def mdf_write(object, filename, lmf2mdf=lmf_mdf, order=mdf_order):
    """! @brief Write an MDF file.
    @param object The LMF instance to convert into MDF output format.
    @param filename The name of the MDF file to write with full path, for instance 'user/output.txt'.
    @param lmf2mdf A Python dictionary describing the mapping between LMF representation and MDF markers. Default value is 'lmf_mdf' dictionary defined in 'src/config/mdf.py'. Please refer to it as an example.
    @param order A Python list defining the order in which MDF markers must be written, for instance ["lx", "ps"]. Default value is 'mdf_order' list defined in 'src/config/mdf.py'.
    """
    mdf_file = open_write(filename)
    # For each MDF marker, get the corresponding LMF value
    if object.__class__.__name__ == "Lexicon":
        for lexical_entry in object.get_lexical_entries():
            for marker in order:
                if type(marker) is list:
                    # There is a bundle of markers
                    group = lmf2mdf[marker[0] + "Group"](lexical_entry)
                    for element in group:
                        # Parse the list of markers
                        for mkr in marker:
                            value = lmf2mdf[mkr](element)
                            write_line(mdf_file, mkr, value)
                    # Group and list of markers have been parsed => go to the next marker
                    continue
                else:
                    value = lmf2mdf[marker](lexical_entry)
                write_line(mdf_file, marker, value)
            # Separate lexical entries from each others with a blank line
            mdf_file.write(EOL)
    else:
        raise OutputError(object, "Object to write must be a Lexicon.")
    mdf_file.close()

def write_line(mdf_file, marker, value):
    """! @brief Write a line into an MDF file.
    @param mdf_file The file to write in.
    @param marker The MDF marker.
    @param value The corresponding value.
    """
    if type(value) is not list:
        # Write the MDF output as follows: "\mdf_marker lmf_value"
        if value is not None:
            mdf_file.write("\\" + marker + " " + value + EOL)
    else:
        # Create a line for each value
        for item in value:
            mdf_file.write("\\" + marker + " " + item + EOL)
