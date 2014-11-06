#! /usr/bin/env python

from config.mdf import mdf_lmf

mdf2lmf = mdf_lmf
mdf2lmf.update({
    "__np" : lambda attributes, np, lexical_entry: process_np(attributes, np, lexical_entry),
    "__ec" : lambda attributes, ec, lexical_entry: process_ec(attributes, ec, lexical_entry)
})

def process_np(attributes, np, lexical_entry):
    if attributes["type"] == "tone":
        lexical_entry.set_tone(np)

def process_ec(attributes, ec, lexical_entry):
    lexical_entry.set_etymology_comment(ec, attributes["lang"])
