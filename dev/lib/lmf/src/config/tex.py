#! /usr/bin/env python

import os
if os.name == 'posix':
    # Unix-style end of line
    eol = '\n'
else:
    # Windows-style end of line
    eol = '\r\n'

## Order in which information must be written in LaTeX output
tex_order = ["Lemma.lexeme", "LexicalEntry.id", "LexicalEntry.partOfSpeech", "LexicalEntry.status"]

## Mapping between LMF representation and LaTeX output
lmf_tex = dict({
    "Lemma.lexeme" : lambda lexical_entry: eol + "\\vspace{1cm} \\hspace{-1cm} {\Large \ipa{" + lexical_entry.get_lexeme() + "}} \\hspace{0.2cm} ",
    "LexicalEntry.id" : lambda lexical_entry: "\\hypertarget{" + str(lexical_entry.get_id()) + "}{}" + eol,
    "LexicalEntry.partOfSpeech" : lambda lexical_entry: "\\textcolor{teal}{\\textit{" + lexical_entry.get_partOfSpeech() + "}}" + eol,
    "LexicalEntry.status" : lambda lexical_entry: ""
})
