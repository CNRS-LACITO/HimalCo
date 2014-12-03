#! /usr/bin/env python

from config.mdf import mdf_lmf, lmf_mdf, mdf_order

FRENCH = "fra"
AUDIO_PATH = "file:///Users/celine/Work/CNRS/workspace/HimalCo/dict/japhug/data/audio/"

## Functions to process some MDF fields (output)
def process_audio(lexical_entry):
    sf = []
    for form_representation in lexical_entry.get_form_representations():
        if form_representation.get_audio() is not None and form_representation.get_audio().get_fileName() is not None:
            sf.append(form_representation.get_audio().get_fileName())
    return sf

mdf2lmf = dict(mdf_lmf)
mdf2lmf.update({
    "hbf"       : lambda hbf, lexical_entry: lexical_entry.set_bibliography(hbf),
    "wav"       : lambda wav, lexical_entry: lexical_entry.set_audio(file_name=AUDIO_PATH + "wav/" + wav + ".wav", quality="very good", audio_file_format="wav"),
    "wav8"      : lambda wav8, lexical_entry: lexical_entry.set_audio(file_name=AUDIO_PATH + "mp3/8_" + wav8 + ".wav", quality="low", audio_file_format="wav"),
    "a"         : lambda a, lexical_entry: lexical_entry.set_spelling_variant(a),
    "constr"    : lambda constr, lexical_entry: None,
    "comit"     : lambda comit, lexical_entry: None,
    "ge"        : lambda ge, lexical_entry: lexical_entry.set_gloss(ge, language=FRENCH)
})

lmf2mdf = dict(lmf_mdf)
lmf2mdf.update({
    "sf": lambda lexical_entry: process_audio(lexical_entry)
})

order = list()
# Copy list of MDF markers without references
def copy_list(in_element, out_list):
    if type(in_element) is list:
        sub_list = list()
        out_list.append(sub_list)
        for element in in_element:
            copy_list(element, sub_list)
    else:
        out_list.append(in_element)
for marker in mdf_order:
    copy_list(marker, order)
order.insert(1, "sf")
