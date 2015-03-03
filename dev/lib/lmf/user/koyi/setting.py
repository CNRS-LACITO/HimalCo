#! /usr/bin/env python

from config.mdf import mdf_lmf, lmf_mdf, mdf_order

mdf2lmf = dict(mdf_lmf)
mdf2lmf.update({
    "a"   : lambda a, lexical_entry: lexical_entry.set_spelling_variant(a)
})

lmf2mdf = dict(lmf_mdf)
lmf2mdf.update({
    "a" : lambda lexical_entry: lexical_entry.get_spelling_variants()
})

order = list(mdf_order)
order.insert(1, "a")
