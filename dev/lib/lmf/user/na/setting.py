#! /usr/bin/env python

from config.mdf import mdf_lmf, lmf_mdf, mdf_order, ps_partOfSpeech
from config.tex import VERNACULAR, ENGLISH, NATIONAL, REGIONAL, partOfSpeech_tex
from output.tex import format_definitions
from utils.io import EOL

## Define languages
import config
FRENCH = "fra"

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
    "lnk"           : "coordinating conjunction",   # linker
    "n"             : "noun",                       # noun
    "Np"            : "possessed noun",             # possessed nouns
    "neg"           : "negation",                   # negative
    "num"           : "numeral",                    # number
    "prep"          : "preposition",                # preposition
    "pro"           : "pronoun",                    # pronoun/pronominal
    "vi.s"          : "stative intransitive verb",  # stative intransitive verb
    # na
    "postp"         : "postposition",               # postposition
    "conj"          : "conjunction"                 # conjunction
})

## Functions to process some MDF fields (input)
def process_np(attributes, np, lexical_entry):
    if attributes["type"] == "tone":
        lexical_entry.set_tone(np)
def process_ec(attributes, ec, lexical_entry):
    lexical_entry.set_etymology_comment(ec, attributes["lang"])
def process_sd(attributes, sd, lexical_entry):
    lexical_entry.set_semantic_domain(sd, attributes["lang"])

def force_caps(text):
    """Force first letter to be in upper case.
    """
    return text[0].upper() + text[1:]

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

mdf2lmf = dict(mdf_lmf)
mdf2lmf.update({
    "__np"  : lambda attributes, np, lexical_entry: process_np(attributes, np, lexical_entry),
    "__ec"  : lambda attributes, ec, lexical_entry: process_ec(attributes, ec, lexical_entry),
    "__sd"  : lambda attributes, sd, lexical_entry: process_sd(attributes, sd, lexical_entry),
    "__sf"  : lambda attributes, sf, lexical_entry: None,
    "__so"  : lambda attributes, so, lexical_entry: None,
    "__va"  : lambda attributes, va, lexical_entry: lexical_entry.set_variant_form(va, type="phonetics"),
    "__nt"  : lambda attributes, nt, lexical_entry: None, # TODO
    "__vf"  : lambda attributes, vf, lexical_entry: None, # TODO
    "__xc"  : lambda attributes, xc, lexical_entry: None, # TODO
    "__cf"  : lambda attributes, cf, lexical_entry: None, # TODO
    "__et"  : lambda attributes, et, lexical_entry: None, # TODO
    "__sn"  : lambda attributes, sn, lexical_entry: None, # TO SOLVE
    "vf"    : lambda vf, lexical_entry: None, # TODO
    "pdf"   : lambda pdf, lexical_entry: lexical_entry.set_paradigm_form(pdf, language=config.xml.French),
    "xf"    : lambda xf, lexical_entry: lexical_entry.add_example(xf, language=config.xml.French),
    "xc"    : lambda xc, lexical_entry: lexical_entry.set_example_comment(xc),
    "gf"    : lambda gf, lexical_entry: lexical_entry.set_gloss(gf, language=config.xml.French),
    # Force first character of definitions to be in upper case
    "dv"    : lambda dv, lexical_entry: lexical_entry.set_definition(force_caps(dv), language=config.xml.vernacular),
    "de"    : lambda de, lexical_entry: lexical_entry.set_definition(force_caps(de), language=config.xml.English),
    "dn"    : lambda dn, lexical_entry: lexical_entry.set_definition(force_caps(dn), language=config.xml.national),
    "dr"    : lambda dr, lexical_entry: lexical_entry.set_definition(force_caps(dr), language=config.xml.regional),
    "df"    : lambda df, lexical_entry: lexical_entry.set_definition(force_caps(df), language=config.xml.French)
})

lmf2mdf = dict(lmf_mdf)
lmf2mdf.update({
    "pdf": lambda paradigm: paradigm.get_paradigm(language=config.xml.French),
    "xf" : lambda context: context.find_written_forms(config.xml.French),
    "xc" : lambda context: context.get_comments(),
    "ec" : lambda lexical_entry: get_ec(lexical_entry),
    "sd" : lambda lexical_entry: get_sd(lexical_entry),
    "df" : lambda sense: sense.find_definitions(config.xml.French),
    "gf" : lambda sense: sense.find_glosses(config.xml.French)
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
order[7].insert(16, "df")
order[7][19].insert(5, "xf")
order[7][19].insert(7, "xc")
order[28].insert(5, "pdf")

## Functions to process some LaTeX fields (output)

my_font = dict({
    VERNACULAR  : lambda text: "\\textcolor{blue}{\\textbf{\ipa{" + text + "}}}",
    ENGLISH     : lambda text: text,
    NATIONAL    : lambda text: "\\textcolor{brown}{\zh{" + text + "}}",
    REGIONAL    : lambda text: "\ipa{" + text + "}",
    FRENCH      : lambda text: text
})

def format_tone(lexical_entry, font):
    import output.tex as tex
    if lexical_entry.get_tones() is not None and len(lexical_entry.get_tones()) != 0:
        return tex.handle_reserved(lexical_entry.get_tones()[0])

def format_definition(lexical_entry, font, language):
    import output.tex as tex
    result = ""
    for sense in lexical_entry.get_senses():
        if sense.find_definitions(language) is not None:
            for definition in sense.find_definitions(language):
                result += font[language](tex.handle_fi(tex.handle_reserved(definition)))
    return result

def format_gloss(lexical_entry, font, language):
    import output.tex as tex
    result = ""
    for sense in lexical_entry.get_senses():
        if sense.find_glosses(language) is not None:
            for gloss in sense.find_glosses(language):
                if language == config.xml.French:
                    result += "Dialecte chinois local~"
                elif language == config.xml.English:
                    result += "Local Chinese dialect"
                result +=  ": " + tex.handle_fi(gloss) + font[NATIONAL](u"\u3002")
    return result

def format_examples(lexical_entry, font, language):
    import output.tex as tex
    result = ""
    for sense in lexical_entry.get_senses():
        for context in sense.get_contexts():
            for example in context.find_written_forms(config.xml.vernacular):
                result += font[VERNACULAR](tex.handle_reserved(example)) + r""" \\""" + EOL
            for example in context.find_written_forms(language):
                result += font[language](tex.handle_reserved(example)) + r""" \\""" + EOL
            for example in context.find_written_forms(config.xml.national):
                result += font[NATIONAL](tex.handle_reserved(example)) + r""" \\""" + EOL
    return result

def tex_fra(lexical_entry, font):
    """<lx> (prononciation~: <lc>~; avec le verbe copule~: <lc <type="with copula">>) TAB <ps> TAB Ton~: <np <type="tone">>.
    <df>.
    <dn>u"\u3002" Dialecte chinois local~: <gr>u"\u3002"
    <xv>
    <xf>
    <xn>
    """
    import output.tex as tex
    return ((r"""%s (prononciation~: %s~; avec le verbe copule~: %s) \hspace{4pt} %s \hspace{4pt} Ton~: %s.""" + EOL + "%s." + EOL + "%s" + my_font[NATIONAL](u"\u3002") + "%s" + EOL + "%s" + "CL~: %s" + EOL) % \
        ("\\vspace{1cm} \\hspace{-1cm} {\Large " + my_font[VERNACULAR](tex.handle_reserved(lexical_entry.get_lexeme())) + "} \\hspace{0.2cm} \\hypertarget{" + unicode(tex.handle_reserved(lexical_entry.get_id())) + "}{}",\
        "LC",\
        "LC AVEC COPULE",\
        "\\textcolor{teal}{\\textsc{" + str(lexical_entry.get_partOfSpeech()) + "}}",\
        format_tone(lexical_entry, my_font),\
        format_definition(lexical_entry, my_font, language=config.xml.French),\
        format_definition(lexical_entry, my_font, language=config.xml.national),\
        format_gloss(lexical_entry, my_font, language=config.xml.French),\
        format_examples(lexical_entry, my_font, language=config.xml.French),\
        "CL")).replace("textsc", "mytextsc")

def tex_eng(lexical_entry, font):
    """<lx> (pronunciation: <lc>; with the copula verb: <lc <type="with copula">>) TAB <ps> TAB Tone: <np <type="tone">>.
    <df>.
    <dn>u"\u3002" Local Chinese dialect: <gr>u"\u3002"
    <xv>
    <xe>
    <xn>
    """
    import output.tex as tex
    return ((r"""%s (pronunciation: %s; with the copula verb: %s) \hspace{4pt} %s \hspace{4pt} Tone: %s.""" + EOL + "%s." + EOL + "%s" + my_font[NATIONAL](u"\u3002") + "%s" + EOL + "%s" + "CL: %s" + EOL) % \
        ("\\vspace{1cm} \\hspace{-1cm} {\Large " + my_font[VERNACULAR](tex.handle_reserved(lexical_entry.get_lexeme())) + "} \\hspace{0.2cm} \\hypertarget{" + unicode(tex.handle_reserved(lexical_entry.get_id())) + "}{}",\
        "LC",\
        "LC WITH COPULA",\
        "\\textcolor{teal}{\\textsc{" + str(lexical_entry.get_partOfSpeech()) + "}}",\
        format_tone(lexical_entry, my_font),\
        format_definition(lexical_entry, my_font, language=config.xml.English),\
        format_definition(lexical_entry, my_font, language=config.xml.national),\
        format_gloss(lexical_entry, my_font, language=config.xml.English),\
        format_examples(lexical_entry, my_font, language=config.xml.French),\
        "CL")).replace("textsc", "mytextsc")
