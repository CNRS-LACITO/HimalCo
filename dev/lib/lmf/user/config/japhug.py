#! /usr/bin/env python

from config.mdf import mdf_lmf, lmf_mdf, mdf_order

mdf2lmf = dict(mdf_lmf)
mdf2lmf.update({
    "hbf" : lambda hbf, lexical_entry: lexical_entry.set_bibliography(hbf)
})

lmf2mdf = dict(lmf_mdf)

order = list(mdf_order)
