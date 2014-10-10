#! /usr/bin/env python

## Mapping between MDF markers and LMF representation (input)
mdf_lmf = dict({
    "lx" : lambda lx, lexical_entry: lexical_entry.set_lexeme(lx),
    "hm" : lambda hm, lexical_entry: lexical_entry.set_homonymNumber(hm),
    "lc" : lambda lc, lexical_entry: None,
    "ph" : lambda ph, lexical_entry: None,
    "se" : lambda se, lexical_entry: None,
    "ps" : lambda ps, lexical_entry: lexical_entry.set_partOfSpeech(ps),
    "pn" : lambda pn, lexical_entry: None,
    "sn" : lambda sn, lexical_entry: None,
    "gv" : lambda gv, lexical_entry: None,
    "dv" : lambda dv, lexical_entry: None,
    "ge" : lambda ge, lexical_entry: None,
    "re" : lambda re, lexical_entry: None,
    "we" : lambda we, lexical_entry: None,
    "de" : lambda de, lexical_entry: None,
    "gn" : lambda gn, lexical_entry: None,
    "rn" : lambda rn, lexical_entry: None,
    "wn" : lambda wn, lexical_entry: None,
    "dn" : lambda dn, lexical_entry: None,
    "gr" : lambda gr, lexical_entry: None,
    "rr" : lambda rr, lexical_entry: None,
    "wr" : lambda wr, lexical_entry: None,
    "dr" : lambda dr, lexical_entry: None,
    "lt" : lambda lt, lexical_entry: None,
    "sc" : lambda sc, lexical_entry: None,
    "rf" : lambda rf, lexical_entry: None,
    "xv" : lambda xv, lexical_entry: None,
    "xe" : lambda xe, lexical_entry: None,
    "xn" : lambda xn, lexical_entry: None,
    "xr" : lambda xr, lexical_entry: None,
    "xg" : lambda xg, lexical_entry: None,
    "uv" : lambda uv, lexical_entry: None,
    "ue" : lambda ue, lexical_entry: None,
    "un" : lambda un, lexical_entry: None,
    "ur" : lambda ur, lexical_entry: None,
    "ev" : lambda ev, lexical_entry: None,
    "ee" : lambda ee, lexical_entry: None,
    "en" : lambda en, lexical_entry: None,
    "er" : lambda er, lexical_entry: None,
    "ov" : lambda ov, lexical_entry: None,
    "oe" : lambda oe, lexical_entry: None,
    "on" : lambda on, lexical_entry: None,
    "or" : lambda OR, lexical_entry: None, # 'or' is a keyword in Python
    "lf" : lambda lf, lexical_entry: None,
    "le" : lambda le, lexical_entry: None,
    "ln" : lambda ln, lexical_entry: None,
    "lr" : lambda lr, lexical_entry: None,
    "sy" : lambda sy, lexical_entry: lexical_entry.create_and_add_related_form(sy, mdf_semanticRelation["sy"]),
    "an" : lambda an, lexical_entry: lexical_entry.create_and_add_related_form(an, mdf_semanticRelation["an"]),
    "mr" : lambda mr, lexical_entry: None,
    "cf" : lambda cf, lexical_entry: lexical_entry.create_and_add_related_form(cf, mdf_semanticRelation["cf"]),
    "ce" : lambda ce, lexical_entry: None,
    "cn" : lambda cn, lexical_entry: None,
    "cr" : lambda cr, lexical_entry: None,
    "mn" : lambda mn, lexical_entry: None,
    "va" : lambda va, lexical_entry: None,
    "ve" : lambda ve, lexical_entry: None,
    "vn" : lambda vn, lexical_entry: None,
    "vr" : lambda vr, lexical_entry: None,
    "bw" : lambda bw, lexical_entry: None,
    "et" : lambda et, lexical_entry: None,
    "eg" : lambda eg, lexical_entry: None,
    "es" : lambda es, lexical_entry: None,
    "ec" : lambda ec, lexical_entry: None,
    "pd" : lambda pd, lexical_entry: None,
    "sg" : lambda sg, lexical_entry: None,
    "pl" : lambda pl, lexical_entry: None,
    "rd" : lambda rd, lexical_entry: None,
    "1s" : lambda a1s, lexical_entry: None,
    "2s" : lambda a2s, lexical_entry: None,
    "3s" : lambda a3s, lexical_entry: None,
    "4s" : lambda a4s, lexical_entry: None,
    "1d" : lambda a1d, lexical_entry: None,
    "2d" : lambda a2d, lexical_entry: None,
    "3d" : lambda a3d, lexical_entry: None,
    "4d" : lambda a4d, lexical_entry: None,
    "1p" : lambda a1p, lexical_entry: None,
    "1e" : lambda a1e, lexical_entry: None,
    "1i" : lambda a1i, lexical_entry: None,
    "2p" : lambda a2p, lexical_entry: None,
    "3p" : lambda a3p, lexical_entry: None,
    "4p" : lambda a4p, lexical_entry: None,
    "tb" : lambda tb, lexical_entry: None,
    "sd" : lambda sd, lexical_entry: None,
    "is" : lambda IS, lexical_entry: None, # 'is' is a keyword in Python
    "th" : lambda th, lexical_entry: None,
    "bb" : lambda bb, lexical_entry: None,
    "pc" : lambda pc, lexical_entry: None,
    "nt" : lambda nt, lexical_entry: None,
    "np" : lambda np, lexical_entry: None,
    "ng" : lambda ng, lexical_entry: None,
    "nd" : lambda nd, lexical_entry: None,
    "na" : lambda na, lexical_entry: None,
    "ns" : lambda ns, lexical_entry: None,
    "nq" : lambda nq, lexical_entry: None,
    "so" : lambda so, lexical_entry: None,
    "st" : lambda st, lexical_entry: lexical_entry.set_status(st),
    "dt" : lambda dt, lexical_entry: lexical_entry.set_date(dt)
})

## Order in which MDF markers must be written (output)
# This is the standard order defined in Appendix B of "Making Dictionaries. A guide to lexicography and the Multi-Dictionary Formatter",
# Software version 1.0, David F. Coward, Charles E. Grimes, SIL International, Waxhaw, North Carolina, 2000
mdf_order = [
    "lx", # lexeme
    "hm", # homonym number
    "lc", # lexical citation
    "ph", # phonetic
    "se", # subentry
    "ps", # part of speech
    "pn", # part of speech-national language
    "sn", # sense number
    "gv", # gloss-vernacular
    "dv", # definition-vernacular
    "ge", # gloss-English
    "re", # reverse-English
    "we", # word level gloss-English
    "de", # definition-English
    "gn", # gloss-national language
    "rn", # reverse-national language
    "wn", # word level gloss-national language
    "dn", # definition-national language
    "gr", # gloss-regional lang. (with \gn)
    "rr", # reverse-regional lang. (with \rn)
    "wr", # word-level gloss-regional (with \wn)
    "dr", # definition-regional lang. (with \dn)
    "lt", # literal meaning
    "sc", # scientific name
    "rf", # reference for example
    "xv", # example sentence-vernacular
    "xe", # example sentence-English
    "xn", # example sentence-national language
    "xr", # example sent.-regional (with \xn)
    "xg", # example sentence-interlinear gloss
    "uv", # usage-vernacular
    "ue", # usage-English
    "un", # usage-national language
    "ur", # usage-regional (combines with \un)
    "ev", # encyclopedic-vernacular
    "ee", # encyclopedic-English
    "en", # encyclopedic-national language
    "er", # encyclopedic-regional language
    "ov", # only (restrictions)-vernacular
    "oe", # only (restrictions)-English
    "on", # only (restrictions)-national language
    "or", # only (restrictions)-regional (with \on)
    "lf", # lexical function
    "le", # lexical function-English
    "ln", # lexical function-national language
    "lr", # lexical function-regional language
    "sy", # synonym
    "an", # antonym
    "mr", # morphemic representation
    "cf", # cross-reference
    "ce", # cross-reference-English gloss
    "cn", # cross-reference-national gloss
    "cr", # cross-reference-regional gloss
    "mn", # main entry form
    "va", # variant form
    "ve", # variant comment-English
    "vn", # variant comment-national language
    "vr", # variant comment-regional language
    "bw", # borrowed word
    "et", # etymology
    "eg", # etymology-gloss
    "es", # etymology-source
    "ec", # etymology-comment
    "pd", # paradigm
    "sg", # singular form
    "pl", # plural form
    "rd", # reduplication
    "1s", # 1st person singular
    "2s", # 2nd person singular
    "3s", # 3rd person singular
    "4s", # singular non-human/non-animate
    "1d", # 1st person dual
    "2d", # 2nd person dual
    "3d", # 3rd person dual
    "4d", # dual non-human/non-animate
    "1p", # 1st person plural-general
    "1e", # 1st person plural-exclusive
    "1i", # 1st person plural-inclusive
    "2p", # 2nd person plural
    "3p", # 3rd person plural
    "4p", # plural non-human/non-animate
    "tb", # table
    "sd", # semantic domain
    "is", # index of semantics
    "th", # thesaurus
    "bb", # bibliographic reference
    "pc", # picture
    "nt", # notes-general
    "np", # notes-phonology
    "ng", # notes-grammar
    "nd", # notes-discourse
    "na", # notes-anthropology
    "ns", # notes-sociolinguistics
    "nq", # notes-questions
    "so", # source
    "st", # status
    "dt", # datestamp
]

## Mapping between LMF representation and MDF markers (output)
lmf_mdf = dict({
    "lx" : lambda lexical_entry: lexical_entry.get_lexeme(),
    "hm" : lambda lexical_entry: lexical_entry.get_homonymNumber(),
    "lc" : lambda lexical_entry: None,
    "ph" : lambda lexical_entry: None,
    "se" : lambda lexical_entry: None,
    "ps" : lambda lexical_entry: lexical_entry.get_partOfSpeech(),
    "pn" : lambda lexical_entry: None,
    "sn" : lambda lexical_entry: None,
    "gv" : lambda lexical_entry: None,
    "dv" : lambda lexical_entry: None,
    "ge" : lambda lexical_entry: None,
    "re" : lambda lexical_entry: None,
    "we" : lambda lexical_entry: None,
    "de" : lambda lexical_entry: None,
    "gn" : lambda lexical_entry: None,
    "rn" : lambda lexical_entry: None,
    "wn" : lambda lexical_entry: None,
    "dn" : lambda lexical_entry: None,
    "gr" : lambda lexical_entry: None,
    "rr" : lambda lexical_entry: None,
    "wr" : lambda lexical_entry: None,
    "dr" : lambda lexical_entry: None,
    "lt" : lambda lexical_entry: None,
    "sc" : lambda lexical_entry: None,
    "rf" : lambda lexical_entry: None,
    "xv" : lambda lexical_entry: None,
    "xe" : lambda lexical_entry: None,
    "xn" : lambda lexical_entry: None,
    "xr" : lambda lexical_entry: None,
    "xg" : lambda lexical_entry: None,
    "uv" : lambda lexical_entry: None,
    "ue" : lambda lexical_entry: None,
    "un" : lambda lexical_entry: None,
    "ur" : lambda lexical_entry: None,
    "ev" : lambda lexical_entry: None,
    "ee" : lambda lexical_entry: None,
    "en" : lambda lexical_entry: None,
    "er" : lambda lexical_entry: None,
    "ov" : lambda lexical_entry: None,
    "oe" : lambda lexical_entry: None,
    "on" : lambda lexical_entry: None,
    "or" : lambda lexical_entry: None,
    "lf" : lambda lexical_entry: None,
    "le" : lambda lexical_entry: None,
    "ln" : lambda lexical_entry: None,
    "lr" : lambda lexical_entry: None,
    "sy" : lambda lexical_entry: lexical_entry.find_related_forms(mdf_semanticRelation["sy"]),
    "an" : lambda lexical_entry: lexical_entry.find_related_forms(mdf_semanticRelation["an"]),
    "mr" : lambda lexical_entry: None,
    "cf" : lambda lexical_entry: lexical_entry.find_related_forms(mdf_semanticRelation["cf"]),
    "ce" : lambda lexical_entry: None,
    "cn" : lambda lexical_entry: None,
    "cr" : lambda lexical_entry: None,
    "mn" : lambda lexical_entry: None,
    "va" : lambda lexical_entry: None,
    "ve" : lambda lexical_entry: None,
    "vn" : lambda lexical_entry: None,
    "vr" : lambda lexical_entry: None,
    "bw" : lambda lexical_entry: None,
    "et" : lambda lexical_entry: None,
    "eg" : lambda lexical_entry: None,
    "es" : lambda lexical_entry: None,
    "ec" : lambda lexical_entry: None,
    "pd" : lambda lexical_entry: None,
    "sg" : lambda lexical_entry: None,
    "pl" : lambda lexical_entry: None,
    "rd" : lambda lexical_entry: None,
    "1s" : lambda lexical_entry: None,
    "2s" : lambda lexical_entry: None,
    "3s" : lambda lexical_entry: None,
    "4s" : lambda lexical_entry: None,
    "1d" : lambda lexical_entry: None,
    "2d" : lambda lexical_entry: None,
    "3d" : lambda lexical_entry: None,
    "4d" : lambda lexical_entry: None,
    "1p" : lambda lexical_entry: None,
    "1e" : lambda lexical_entry: None,
    "1i" : lambda lexical_entry: None,
    "2p" : lambda lexical_entry: None,
    "3p" : lambda lexical_entry: None,
    "4p" : lambda lexical_entry: None,
    "tb" : lambda lexical_entry: None,
    "sd" : lambda lexical_entry: None,
    "is" : lambda lexical_entry: None,
    "th" : lambda lexical_entry: None,
    "bb" : lambda lexical_entry: None,
    "pc" : lambda lexical_entry: None,
    "nt" : lambda lexical_entry: None,
    "np" : lambda lexical_entry: None,
    "ng" : lambda lexical_entry: None,
    "nd" : lambda lexical_entry: None,
    "na" : lambda lexical_entry: None,
    "ns" : lambda lexical_entry: None,
    "nq" : lambda lexical_entry: None,
    "so" : lambda lexical_entry: None,
    "st" : lambda lexical_entry: lexical_entry.get_status(),
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
