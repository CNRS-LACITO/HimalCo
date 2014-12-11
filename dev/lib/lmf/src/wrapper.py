#! /usr/bin/env python

"""! @package lmf.src.wrapper Contains one main function, wrapper(), which runs another function which should be a user function. If the library raises an exception, wrapper() will restore the terminal to a sane state so you can read the resulting traceback.
"""

# Add lib/lmf/src/ folder to path
import sys
sys.path.append('./src')

## Functions to read from a file: MDF, XML LMF
from input.mdf import mdf_read
from input.xml_lmf import xml_lmf_read as lmf_read

## Functions to write into a file: MDF, XML LMF, LaTeX, doc
from output.mdf import mdf_write
from output.xml_lmf import xml_lmf_write as lmf_write
from output.tex import tex_write
from output.doc import doc_write

from utils.error_handling import Error
from utils.log import log

def wrapper(func, *args, **kwds):
    """! @brief Wrapper function that calls another function, restoring normal behavior on error.
    @param func Callable object.
    @param args Arguments passed to 'func' as its first argument.
    @param kwds Other arguments passed to 'func'.
    """
    ## Function variable
    wrapper.lexical_resource = None
    ## As this is a user function, it is executed under 'try' statement to catch and handle exceptions
    try:
        from core.lexical_resource import LexicalResource
        if wrapper.lexical_resource is None:
            # Create a Lexical Resource only once
            wrapper.lexical_resource = LexicalResource()
        object = func(*args, **kwds)
        if object.__class__.__name__ == "LexicalResource":
            return object
        elif object.__class__.__name__ == "Lexicon":
            # Attach lexicon to the lexical resource
            wrapper.lexical_resource.add_lexicon(object)
            return wrapper.lexical_resource
    except Error as exception:
        ## A library error has occured
        exception.handle()
    except SystemExit:
        ## The library decided to stop execution
        raise
    except:
        ## A system error has occured
        import sys
        sys.stderr.write("Unexpected error: " + str(sys.exc_info()[0]) + "\n")
        raise
    else:
        ## Nominal case
        pass
    finally:
        ## Set everything back to normal and release created objects if any
        pass

def read_mdf(*args, **kwds):
    # An MDF file contains one lexicon only, but wrapper() function encapsulates it into a lexical resource
    lexical_resource = wrapper(mdf_read, *args, **kwds)
    log("Successfully created %s LMF entries from MDF file '%s'." % (lexical_resource.lexicon[-1].count_lexical_entries(), args[0]))
    return lexical_resource

def read_xml_lmf(*args, **kwds):
    # An XML LMF file contains one lexical resource, itself containing lexicon(s)
    lexical_resource = wrapper(lmf_read, *args, **kwds)
    # Count total number of entries to report to user
    entries_nb = 0
    for lexicon in lexical_resource.get_lexicons():
        entries_nb += lexicon.count_lexical_entries()
        # Verify lexicon coherence
        lexicon.check_cross_references()
    log("Successfully created %s LMF entries from XML LMF file '%s'." % (entries_nb, args[0]))
    return lexical_resource

def write_mdf(*args, **kwds):
    # As an MDF file can only contain one lexicon, create as many MDF files as lexicons in the lexical resource (TODO: rename files)
    for lexicon in args[0].get_lexicons():
        wrapper(mdf_write, lexicon, *args[1:], **kwds)
        log("Successfully wrote %s LMF entries into MDF file '%s'." % (lexicon.count_lexical_entries(), args[1]))

def write_xml_lmf(*args, **kwds):
    # An XML LMF file contains one lexical resource, itself containing lexicon(s)
    wrapper(lmf_write, *args, **kwds)
    # Count total number of entries to report to user
    entries_nb = 0
    for lexicon in args[0].get_lexicons():
        entries_nb += lexicon.count_lexical_entries()
    log("Successfully wrote %s LMF entries into XML LMF file '%s'." % (entries_nb, args[1]))

def write_tex(*args, **kwds):
    # A LaTeX file contains one or several lexicons and informations about the lexical resource
    wrapper(tex_write, *args, **kwds)
    # Count total number of entries to report to user
    entries_nb = 0
    for lexicon in args[0].get_lexicons():
        entries_nb += lexicon.count_lexical_entries()
    log("Successfully wrote %s LMF entries into LaTeX file '%s'." % (entries_nb, args[1]))

def write_doc(*args, **kwds):
    # A document file contains one or several lexicons and informations about the lexical resource
    wrapper(doc_write, *args, **kwds)
    # Count total number of entries to report to user
    entries_nb = 0
    for lexicon in args[0].get_lexicons():
        entries_nb += lexicon.count_lexical_entries()
    log("Successfully wrote %s LMF entries into document file '%s'." % (entries_nb, args[1]))
