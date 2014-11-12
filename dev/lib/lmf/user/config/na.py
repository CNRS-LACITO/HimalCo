#! /usr/bin/env python

from config.mdf import mdf_lmf, lmf_mdf, mdf_order

FRENCH = "fra"

mdf2lmf = mdf_lmf
mdf2lmf.update({
    "__np" : lambda attributes, np, lexical_entry: process_np(attributes, np, lexical_entry),
    "__ec" : lambda attributes, ec, lexical_entry: process_ec(attributes, ec, lexical_entry),
    "pdf"  : lambda pdf, lexical_entry: lexical_entry.set_paradigm_form(pdf, language=FRENCH)
})

def process_np(attributes, np, lexical_entry):
    if attributes["type"] == "tone":
        lexical_entry.set_tone(np)

def process_ec(attributes, ec, lexical_entry):
    lexical_entry.set_etymology_comment(ec, attributes["lang"])

lmf2mdf = lmf_mdf
lmf2mdf.update({
    "pdf" : lambda paradigm: paradigm.get_paradigm(language=FRENCH)
})

order = mdf_order
order[28].insert(5, "pdf")
