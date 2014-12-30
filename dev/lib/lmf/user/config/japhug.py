#! /usr/bin/env python
# -*- coding: utf-8 -*-

from config.mdf import mdf_lmf, lmf_mdf, mdf_order, mdf_semanticRelation, VERNACULAR, NATIONAL, ps_partOfSpeech
from common.range import partOfSpeech_range
from config.tex import lmf_to_tex, partOfSpeech_tex

FRENCH = "fra"
AUDIO_PATH = "file:///Users/celine/Work/CNRS/workspace/HimalCo/dict/japhug/data/audio/"

ranks = dict({'':0,
    'a':1,
    'ɤ':2,
    'b':3, 'β':3.1,
    'c':4,
    'ɕ':5,
    'd':6,
    'e':7,
    'f':8,
    'g':9,
    'ɣ':10,
    'ɢ':11,
    'H':12, 'h':12,'ɦ':12.1,
    'i':13,
    'j':14,
    'ɟ':15,
    'K':16, 'k':16,
    'l':17,
    'ɬ':18,
    'm':19,
    'n':20,
    'ɳ':21,'ɲ':21.1,
    'ŋ':22,
    'ɴ':23,
    'o':24,
    'p':25,
    'q':26,
    'r':27,
    'ʀ':28,'ʁ':28.1,
    's':29,
    'ʂ':30,
    't':31,
    'u':32,
    'ɯ':33,
    'v':34,
    'w':35,
    'x':36,
    'χ':37,
    'y':38,
    'z':39,
    'ʐ':40,
    'ʑ':41,
    'ʕ':42,
    # Special characters
    '_':43.1, '-':43.2})
unicode_ranks = ({})
for key in ranks.keys():
    unicode_ranks.update({key.decode(encoding='utf8'):ranks[key]})

## Mapping between 'ps' MDF marker value and LMF part of speech LexicalEntry attribute value (input)
ps2partOfSpeech = ps_partOfSpeech
ps2partOfSpeech.update({
    # HimalCo
    "adj"           : "adjective",                  # adjective
    "adv"           : "adverb",                     # adverb(ial)
    "class"         : "classifier",                 # classifier (MDF)
    "clf"           : "classifier",                 # classifier (Leipzig)
    "cnj"           : "conjunction",                # conjunction
    "disc.PTCL"     : "particle",                   # discourse particle
    "ideo"          : "ideophone",                  # ideophones
    "intj"          : "interjection",               # interjection
    "interj"        : "interjection",               # interjection -> khaling
    "lnk"           : None,                         # linker
    "n"             : "noun",                       # noun
    "Np"            : None,                         # possessed nouns
    "_poss._pref"   : None,                         # possessed nouns -> koyi
    "neg"           : "negation",                   # negative
    "num"           : "numeral",                    # number
    "prep"          : "preposition",                # preposition
    "pro"           : "pronoun",                    # pronoun/pronominal
    "v"             : "verb",                       # verb
    "vi"            : "intransitive verb",          # intransitive verb
    "vi.s"          : None,                         # stative intransitive verb
    "vr"            : "reflexive verb",             # reflexive/quasi-reflexive/intradirective verb
    "vt"            : "transitive verb",            # transitive verb
    "vt/i"          : "bitransistive verb",         # ambitransitive verb: labial verb
    # japhug
    "cl"            : "classifier",                 # classifier
    "conj"          : "conjunction",                # conjunction
    "expression"    : None,                         #
    "idph"          : "ideophone",                  # ideophones
    "idph.1"        : "ideophone",                  # ideophones
    "idph.2"        : "ideophone",                  # ideophones
    "idph.3"        : "ideophone",                  # ideophones
    "idph.4"        : "ideophone",                  # ideophones
    "idph.5"        : "ideophone",                  # ideophones
    "idph.6"        : "ideophone",                  # ideophones
    "idph.7"        : "ideophone",                  # ideophones
    "idph.8"        : "ideophone",                  # ideophones
    "n N"           : "noun",                       # noun
    "nq"            : "noun",                       # noun
    "np"            : None,                         # possessed nouns
    "nP"            : None,                         # possessed nouns
    "Posp"          : None,                         # possessed nouns
    "Post"          : None,                         # possessed nouns
    "postp"         : None,                         # possessed nouns
    "quant"         : "numeral",                    # number
    "part"          : "particle",                   # discourse particle
    "Part"          : "particle",                   # discourse particle
    "vi-"           : "intransitive verb",          # intransitive verb
    "vinh"          : None,                         # stative intransitive verb
    "vStat"         : None,                         # stative intransitive verb
    "vst"           : None,                         # stative intransitive verb
    "vs"            : None,                         # stative intransitive verb
    "vl"            : "bitransistive verb",         # labial verb
    "vlb"           : "bitransistive verb",         # labial verb
    "vlab"          : "bitransistive verb",         # labial verb
    "T"             : None,                         # ?
    "indef"         : None                          # undefined
})

## Possible values allowed for LMF part of speech LexicalEntry attribute
partOfSpeech_range.update([
])

## Functions to process some MDF fields (input)
def remove_char(value):
    """Function to remove '_', '^', '$', '&' character at the beginning of 'lx', 'se', 'a', 'xv', 'cf' MDF fields.
    """
    return value.lstrip('_^$&')

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
    "a"         : lambda a, lexical_entry: lexical_entry.set_spelling_variant(remove_char(a)),
    "ge"        : lambda ge, lexical_entry: lexical_entry.set_gloss(ge, language=FRENCH),
    "lx"        : lambda lx, lexical_entry: lexical_entry.set_lexeme(remove_char(lx)),
    "se"        : lambda se, lexical_entry: lexical_entry.create_and_add_related_form(remove_char(se), mdf_semanticRelation["se"]),
    "xv"        : lambda xv, lexical_entry: lexical_entry.create_example(remove_char(xv), language=VERNACULAR),
    "cf"        : lambda cf, lexical_entry: lexical_entry.create_and_add_related_form(remove_char(cf), mdf_semanticRelation["cf"]),
    "ps"        : lambda ps, lexical_entry: lexical_entry.set_partOfSpeech(ps, range=partOfSpeech_range, mapping=ps2partOfSpeech)
})

lmf2mdf = dict(lmf_mdf)
lmf2mdf.update({
    "sf" : lambda lexical_entry: process_audio(lexical_entry),
    "gf" : lambda sense: sense.find_glosses(FRENCH)
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
order[7].insert(15, "gf")
order.insert(1, "sf")

## Mapping between LMF part of speech LexicalEntry attribute value and LaTeX layout (output)
partOfSpeech2tex = partOfSpeech_tex
partOfSpeech2tex.update({
    "ideophone"     : "idph",
    "indefinite"    : "indf" # Leipzip
})

def lmf2tex(lexical_entry, font):
    return lmf_to_tex(lexical_entry, font, partOfSpeech_mapping=partOfSpeech2tex, languages=[VERNACULAR, FRENCH, NATIONAL])
