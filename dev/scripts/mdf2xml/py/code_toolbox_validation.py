import nltk

# Natural Language Toolkit: code_toolbox_validation

grammar = nltk.parse_cfg('''
  S -> Head PS Glosses Comment Date Sem_Field Examples Paradigmes Audio Usage Definition Unknown
  Head -> Header Lexeme Root
  Header -> "_sh"
  Lexeme -> "lx" | "a" | "va" | "sy" | "an" | "cf"
  Root -> "rt" |
  PS -> "ps" | "se" | "se2"
  Glosses -> Gloss Glosses |
  Gloss -> "gn" | "ge" | "tkp" | "eng"
  Date -> "dt"
  Sem_Field -> "sf"
  Examples -> Example Ex_Pidgin Ex_English Examples |
  Example -> "ex" | "example" | "xn"
  Ex_Pidgin -> "xp"
  Ex_English -> "xe"
  Comment -> "cmt" | "nt" | "nq" | "ng"
  Paradigmes -> "_1s" | "_1p" | "_2s" | "_2p" | "_3s" | "_3p" | "_1d" | "_1e" | "_4s" | "_3d"
  Audio -> "sf" | "wav" |
  Usage -> "ue" | "un" | "uv" | "u"
  Definition -> "de" | "dn" | "dv" |
  Unknown -> "vn" | "vr"
  ''')

def validate_lexicon(grammar, lexicon, ignored_tags):
    rd_parser = nltk.RecursiveDescentParser(grammar)
    for entry in lexicon:
        marker_list = [field.tag for field in entry if field.tag not in ignored_tags]
        if rd_parser.nbest_parse(marker_list):
            print "+", ':'.join(marker_list) # [_accepted-entries]
        else:
            print "-", ':'.join(marker_list) # [_rejected-entries]

