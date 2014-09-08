#! /usr/bin/env python

mdf2lmf = dict({
    "lx" : lambda lx, lexical_entry: lexical_entry.set_lexeme(lx),
    "ps" : lambda ps, lexical_entry: lexical_entry.set_partOfSpeech(ps),
    "st" : lambda st, lexical_entry: lexical_entry.set_status(st)
})
