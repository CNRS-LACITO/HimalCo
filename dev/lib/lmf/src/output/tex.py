#! /usr/bin/env python

from config.tex import lmf_tex, tex_order
from utils.io import open_read, open_write, EOL

def compute_header(preamble):
    """! @brief Create LaTeX header.
    @param preamble The name of the LaTeX file with full path containing the LaTeX header of the document, for instance 'user/config/japhug.tex'.
    @return A Python string containing read information.
    """
    header = ""
    if preamble is not None:
        hdr = open_read(preamble)
        header = hdr.read()
        hdr.close()
    return header

def tex_write(object, filename, preamble=None, lmf2tex=lmf_tex, order=tex_order):
    """! @brief Write a LaTeX file.
    @param object The LMF instance to convert into LaTeX output format.
    @param filename The name of the LaTeX file to write with full path, for instance 'user/output.tex'.
    @param preamble The name of the LaTeX file with full path containing the LaTeX header of the document, for instance 'user/config/japhug.tex'. Deafult value is None.
    @param lmf2tex A Python dictionary describing the mapping between LMF representation and LaTeX commands. Default value is 'lmf_tex' dictionary defined in 'src/config/tex.py'. Please refer to it as an example.
    @param order A Python list defining the order in which LMF information must be written, for instance  ["Lemma.lexeme", "LexicalEntry.partOfSpeech"]. Default value is 'tex_order' list defined in 'src/config/tex.py'.
    """
    tex_file = open_write(filename)
    # Add file header if any
    tex_file.write(compute_header(preamble))
    # Insert LaTeX commands to create a document
    tex_file.write(EOL + "\\begin{document}" + EOL)
    tex_file.write("\\maketitle" + EOL)
    tex_file.write("\\newpage" + EOL)
    tex_file.write("\\begin{multicols}{2}" + EOL)
    # For each element to write, get the corresponding LMF value
    if object.__class__.__name__ == "Lexicon":
        for lexical_entry in object.get_lexical_entries():
            for attribute in order:
                tex_file.write(lmf2tex[attribute](lexical_entry))
            # Separate lexical entries from each others with a blank line
            tex_file.write(EOL)
    else:
        raise AttributeError(0, __file__, "Object to write must be a Lexicon.")
    # Insert LaTeX commands to finish the document properly
    tex_file.write("\end{multicols}" + EOL)
    tex_file.write("\end{document}" + EOL)
    tex_file.close()
