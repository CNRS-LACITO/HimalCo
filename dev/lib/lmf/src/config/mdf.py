#! /usr/bin/env python

## Mapping between MDF markers and LMF representation (input)
mdf_lmf = dict({
    "lx" : lambda lx, lexical_entry: lexical_entry.set_lexeme(lx),
    "ps" : lambda ps, lexical_entry: lexical_entry.set_partOfSpeech(ps),
    "st" : lambda st, lexical_entry: lexical_entry.set_status(st)
})

## Order in which MDF markers must be written (output)
mdf_order = ["lx", "ps", "st"]

## Mapping between LMF representation and MDF markers (output)
lmf_mdf = dict({
    "lx" : lambda lexical_entry: lexical_entry.get_lexeme(),
    "ps" : lambda lexical_entry: lexical_entry.get_partOfSpeech(),
    "st" : lambda lexical_entry: lexical_entry.get_status()
})
