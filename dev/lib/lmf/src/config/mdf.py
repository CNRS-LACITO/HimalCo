#! /usr/bin/env python

## Mapping between MDF markers and LMF representation (input)
mdf_lmf = dict({
    "lx" : lambda lx, lexical_entry: lexical_entry.set_lexeme(lx),
    "ps" : lambda ps, lexical_entry: lexical_entry.set_partOfSpeech(ps),
    "st" : lambda st, lexical_entry: lexical_entry.set_status(st),
    "sy" : lambda sy, lexical_entry: lexical_entry.create_and_add_related_form(sy, mdf_semanticRelation["sy"]),
    "an" : lambda an, lexical_entry: lexical_entry.create_and_add_related_form(an, mdf_semanticRelation["an"]),
    "cf" : lambda cf, lexical_entry: lexical_entry.create_and_add_related_form(cf, mdf_semanticRelation["cf"]),
    "dt" : lambda dt, lexical_entry: lexical_entry.set_date(dt)
})

## Order in which MDF markers must be written (output)
mdf_order = ["lx", "ps", "st", "sy", "an", "cf", "dt"]

## Mapping between LMF representation and MDF markers (output)
lmf_mdf = dict({
    "lx" : lambda lexical_entry: lexical_entry.get_lexeme(),
    "ps" : lambda lexical_entry: lexical_entry.get_partOfSpeech(),
    "st" : lambda lexical_entry: lexical_entry.get_status(),
    "sy" : lambda lexical_entry: lexical_entry.find_related_forms(mdf_semanticRelation["sy"]),
    "an" : lambda lexical_entry: lexical_entry.find_related_forms(mdf_semanticRelation["an"]),
    "cf" : lambda lexical_entry: lexical_entry.find_related_forms(mdf_semanticRelation["cf"]),
    "dt" : lambda lexical_entry: lexical_entry.get_date()
})

## Mapping between 'ps' MDF marker value and LMF part of speech LexicalEntry attribute value (input)
ps_partOfSpeech = dict({
    "adj"       : "adjective",                  # adjective
    "adv"       : "adverb",                     # adverb(ial)
    "class"     : "classifier",                 # classifier (MDF)
    "clf"       : "classifier",                 # classifier (Leipzig)
    "cnj"       : "conjunction",                # conjunction
    "disc.PTCL" : "particle",                   # discourse particle
    "ideo"      : "ideophone",                  # ideophones
    "intj"      : "interjection",               # interjection
    "lnk"       : "linker",                     # linker
    "n"         : "noun",                       # noun
    "Np"        : "possessive pronouns",        # possessed nouns
    "neg"       : "negation",                   # negative
    "num"       : "numeral",                    # number
    "prep"      : "preposition",                # preposition
    "pro"       : "pronoun",                    # pronoun/pronominal
    "v"         : "verb",                       # verb
    "vi"        : "intransitive verb",          # intransitive verb
    "vi.s"      : "stative intransitive verb",  # stative intransitive verb
    "vr"        : "reflexive verb",             # reflexive/quasi-reflexive/intradirective verb
    "vt"        : "transitive verb",            # transitive verb
    "vt/i"      : "bitransistive verb"          # ambitransitive verb
})

## Mapping between MDF markers and LMF semantic relation RelatedForm attribute value (input)
mdf_semanticRelation = dict({
    "sy" : "synonym",
    "an" : "antonym",
    "cf <hm>" : "homonym",
    "cf <et>" : "etymology",
    "se" : "subentry",
    "mn" : "main entry",
    "cf" : "simple link",
    "lf" : None,
    "ev" : None,
    "ee" : None,
    "en" : None,
    "er" : None
    # "derived form",
    # "root",
    # "stem",
    # "collocation"
})

## Mapping between 'pdl' MDF marker value and LMF paradigm label Paradigm attribute value (input)
pdl_paradigmLabel = dict({
    "la"        : "lexicalized affix",
    "cc"        : "conjugation class",
    "past"      : "theme of the past",
    "comit"     : "comitative",
    "constr"    : "construction",
    "dir"       : "directional",
    "ir"        : "irregularity"
})
