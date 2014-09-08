#! /usr/bin/env python

## Order in which information must be written in LaTeX output
tex_order = ["Lemma.lexeme", "LexicalEntry.id", "LexicalEntry.partOfSpeech", "LexicalEntry.status"]

## Mapping between LMF representation and LaTeX output
lmf_tex = dict({
    "Lemma.lexeme" : lambda lexical_entry: "\n\\vspace{1cm} \\hspace{-1cm} {\Large \ipa{" + lexical_entry.get_lexeme() + "}} \\hspace{0.2cm} ",
    "LexicalEntry.id" : lambda lexical_entry: "\\hypertarget{" + str(lexical_entry.get_id()) + "}{}\n",
    "LexicalEntry.partOfSpeech" : lambda lexical_entry: "\\textcolor{teal}{\\textit{" + lexical_entry.get_partOfSpeech() + "}}\n",
    "LexicalEntry.status" : lambda lexical_entry: ""
})
