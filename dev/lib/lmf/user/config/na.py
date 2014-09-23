#! /usr/bin/env python

mdf2lmf = dict({
    "lx" : lambda lx, lexical_entry: lexical_entry.set_lexeme(lx),
    "ps" : lambda ps, lexical_entry: lexical_entry.set_partOfSpeech(ps),
    "st" : lambda st, lexical_entry: lexical_entry.set_status(st),
    "sy" : lambda sy, lexical_entry: lexical_entry.add_related_form(lexical_entry.create_related_form(sy, "synonym")),
    "an" : lambda an, lexical_entry: lexical_entry.add_related_form(lexical_entry.create_related_form(an, "antonym")),
    "cf" : lambda cf, lexical_entry: lexical_entry.add_related_form(lexical_entry.create_related_form(cf, "simple link"))
})
