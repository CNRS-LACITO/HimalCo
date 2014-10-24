#! /usr/bin/env python

from config.mdf import mdf_lmf

mdf2lmf = mdf_lmf
mdf2lmf.update({
    "np" : lambda attributes, np, lexical_entry: process_np(attributes, np, lexical_entry)
})

def process_np(attributes, np, lexical_entry):
    if attributes["type"] == "tone":
        lexical_entry.set_tone(np)
