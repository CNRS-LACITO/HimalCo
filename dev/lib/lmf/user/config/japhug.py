#! /usr/bin/env python
# -*- coding: utf-8 -*-

from config.mdf import mdf_lmf, lmf_mdf, mdf_order, mdf_semanticRelation, VERNACULAR, NATIONAL, ps_partOfSpeech
from common.range import partOfSpeech_range
from config.tex import lmf_to_tex, partOfSpeech_tex

FRENCH = "fra"
AUDIO_PATH = "file:///Users/celine/Work/CNRS/workspace/HimalCo/dict/japhug/data/audio/"

ranks = dict({'':0,
    'A':1.1, 'a':1.2, 'æ':1.3, 'ɑ':1.4, 'ɐ':1.5,
    'ɤ':2,
    'B':3.1, 'b':3.2, 'β':3.3, 'ɓ':3.4, 'ʙ':3.5,
    'C':4.1, 'c':4.2,
    'ɕ':5.1, 'ç':5.2,
    'D':6.1, 'd':6.2, 'ɖ':6.3, 'ð':6.4, 'ɗ':6.5,
    'E':7.1, 'e':7.2, 'ɛ':7.3, 'ə':7.4, 'ɜ':7.5, 'œ':7.6, 'ɶ':7.7, 'ɘ':7.8, 'ɞ':7.9,
    'F':8.1, 'f':8.2, 'ɸ':8.3,
    'G':9.1, 'g':9.2, 'ɡ':9.3,
    'ɣ':10.1, 'ɠ':10.2,
    'ɢ':11.1, 'ʛ':11.1,
    'H':12.1, 'h':12.2, 'ɦ':12.3, 'ɥ':12.4, 'ħ':12.5, 'ʜ':12.6, 'ɧ':12.7,
    'I':13.1, 'i':13.2, 'ɪ':13.3, 'ɨ':13.4,
    'J':14.1, 'j':14.2, 'ʝ':14.3,
    'ɟ':15.1, 'ʄ':15.2,
    'K':16.1, 'k':16.2,
    'L':17.1, 'l':17.2, 'ɭ':17.3,
    'ɬ':18.1, 'ɮ':18.2, 'ʎ':18.3, 'ʟ':18.4, 'ɺ':18.5,
    'M':19.1, 'm':19.2, 'ɱ':19.3,
    'N':20.1, 'n':20.2,
    'ɳ':21.1, 'ɲ':21.2,
    'ŋ':22,
    'ɴ':23,
    'O':24.1, 'o':24.2, 'ɔ':24.3, 'ɒ':24.4, 'ø':24.5, 'ɵ':24.6,
    'P':25.1, 'p':25.2, 'ʘ':25.3,
    'Q':26.1, 'q':26.2,
    'R':27.1, 'r':27.2, 'ɽ':27.3, 'ɹ':27.4, 'ɾ':27.5, 'ɻ':27.6,
    'ʀ':28.1, 'ʁ':28.2,
    'S':29.1, 's':29.2,
    'ʂ':30.1, 'ʃ':30.2,
    'T':31.1, 't':31.2, 'ʈ':31.3, 'θ':31.4,
    'U':32.1, 'u':32.2, 'ʊ':32.3,
    'ɯ':33.1, 'ʌ':33.2, 'ʉ':33.3,
    'V':34.1, 'v':34.2, 'ʋ':34.3,
    'W':35.1, 'w':35.2, 'ʍ':35.3, 'ɰ':35.4,
    'X':36.1, 'x':36.2,
    'χ':37,
    'Y':38.1, 'y':38.2, 'ʏ':38.3,
    'Z':39.1, 'z':39.2,
    'ʐ':40.1, 'ʒ':40.2,
    'ʑ':41,
    'ʕ':42.1, 'ʢ':42.2, 'ʔ':42.3, 'ʡ':42.4,
    'ǃ':43.1, 'ǀ':43.2, 'ǂ':43.3, 'ǁ':43.4,
    '_':44,
    # Special characters
    '*':45.1, '˭':45.2, 'ʰ':45.3, ' ̩':45.4, '‑':45.5, '-':45.6})
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
