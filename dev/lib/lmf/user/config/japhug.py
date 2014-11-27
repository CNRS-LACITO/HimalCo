#! /usr/bin/env python

from config.mdf import mdf_lmf, lmf_mdf, mdf_order

FRENCH = "fra"

mdf2lmf = dict(mdf_lmf)
mdf2lmf.update({
    "hbf"       : lambda hbf, lexical_entry: lexical_entry.set_bibliography(hbf),
    "wav"       : lambda wav, lexical_entry: None,
    "wav8"      : lambda wav8, lexical_entry: None,
    "a"         : lambda a, lexical_entry: lexical_entry.set_spelling_variant(a),
    "constr"    : lambda constr, lexical_entry: None,
    "comit"     : lambda comit, lexical_entry: None,
    "ge"        : lambda ge, lexical_entry: lexical_entry.set_gloss(ge, language=FRENCH)
})

lmf2mdf = dict(lmf_mdf)

order = list(mdf_order)
