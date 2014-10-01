#! /usr/bin/env python

"""! @package lmf.src.wrapper Contains one main function, wrapper(), which runs another function which should be a user function. If the library raises an exception, wrapper() will restore the terminal to a sane state so you can read the resulting traceback.
"""

# Add lib/lmf/src/ folder to path
import sys
sys.path.append('./src')

## Functions to read from a file: MDF, XML LMF
from input.mdf import mdf_read
from input.xml_lmf import xml_lmf_read as lmf_read

## Functions to write into a file: MDF, XML LMF, LaTeX
from output.mdf import mdf_write
from output.xml_lmf import xml_lmf_write as lmf_write
from output.tex import tex_write

from utils.error_handling import Error
from utils.log import log

def wrapper(func, *args, **kwds):
    """! @brief Wrapper function that calls another function, restoring normal behavior on error.
    @param func Callable object.
    @param args Arguments passed to 'func' as its first argument.
    @param kwds Other arguments passed to 'func'.
    """
    ## As this is a user function, it is executed under 'try' statement to catch and handle exceptions
    try:
        return func(*args, **kwds)
    except Error as exception:
        ## A library error has occured
        exception.handle()
    except:
        ## A system error has occured
        import sys
        sys.stderr.write("Unexpected error: " + str(sys.exc_info()[0]))
        raise
    else:
        ## Nominal case
        print "else"
    finally:
        ## Set everything back to normal
        # Release created objects if any
        if 'lexicon' in locals():
            del lexicon

def read_mdf(*args, **kwds):
    lexicon = wrapper(mdf_read, *args, **kwds)
    log("Successfully created %s LMF entries from MDF file '%s'." % (lexicon.count_lexical_entries(), args[0]))
    return lexicon

def read_xml_lmf(*args, **kwds):
    lexicon = wrapper(lmf_read, *args, **kwds)
    log("Successfully created %s LMF entries from MDF file '%s'." % (lexicon.count_lexical_entries(), args[0]))
    return lexicon

def write_mdf(*args, **kwds):
    wrapper(mdf_write, *args, **kwds)
    log("Successfully wrote %s LMF entries into MDF file '%s'." % (args[0].count_lexical_entries(), args[1]))

def write_xml_lmf(*args, **kwds):
    wrapper(lmf_write, *args, **kwds)
    log("Successfully wrote %s LMF entries into XML LMF file '%s'." % (args[0].count_lexical_entries(), args[1]))

def write_tex(*args, **kwds):
    wrapper(tex_write, *args, **kwds)
    log("Successfully wrote %s LMF entries into LaTeX file '%s'." % (args[0].count_lexical_entries(), args[1]))
