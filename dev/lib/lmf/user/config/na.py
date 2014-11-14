#! /usr/bin/env python

from config.mdf import mdf_lmf, lmf_mdf, mdf_order
from utils.io import EOL

FRENCH = "fra"

mdf2lmf = mdf_lmf
mdf2lmf.update({
    "__np" : lambda attributes, np, lexical_entry: process_np(attributes, np, lexical_entry),
    "__ec" : lambda attributes, ec, lexical_entry: process_ec(attributes, ec, lexical_entry),
    "__sd" : lambda attributes, sd, lexical_entry: process_sd(attributes, sd, lexical_entry),
    "pdf"  : lambda pdf, lexical_entry: lexical_entry.set_paradigm_form(pdf, language=FRENCH),
    "xf" : lambda xf, lexical_entry: lexical_entry.add_example(xf, language=FRENCH),
    "xc" : lambda xc, lexical_entry: lexical_entry.set_example_comment(xc)
})

def process_np(attributes, np, lexical_entry):
    if attributes["type"] == "tone":
        lexical_entry.set_tone(np)

def process_ec(attributes, ec, lexical_entry):
    lexical_entry.set_etymology_comment(ec, attributes["lang"])

def process_sd(attributes, sd, lexical_entry):
    lexical_entry.set_semantic_domain(sd, attributes["lang"])

## Functions to process some MDF fields (output)
def get_ec(lexical_entry):
    ec = lexical_entry.get_etymology_comment()
    if lexical_entry.get_term_source_language() is not None:
        ec = "<lang=\"" + lexical_entry.get_term_source_language() + "\">" + " " + ec
    return ec
def get_sd(lexical_entry):
    sd = ''
    sd_fr = lexical_entry.get_semantic_domains("fr")
    if sd_fr != []:
        sd += "<lang=\"fra\"> " + sd_fr[0]
    sd_en = lexical_entry.get_semantic_domains("en")
    if sd_en != []:
        sd += EOL + "\\sd <lang=\"eng\"> " + sd_en[0]
    if sd != '':
        return sd

lmf2mdf = lmf_mdf
lmf2mdf.update({
    "pdf" : lambda paradigm: paradigm.get_paradigm(language=FRENCH),
    "xf" : lambda context: context.find_written_forms(FRENCH),
    "xc" : lambda context: context.get_comments(),
    "ec" : lambda lexical_entry: get_ec(lexical_entry),
    "sd" : lambda lexical_entry: get_sd(lexical_entry)
})

order = mdf_order
order[28].insert(5, "pdf")
order[7][17].insert(5, "xf")
order[7][17].insert(7, "xc")
