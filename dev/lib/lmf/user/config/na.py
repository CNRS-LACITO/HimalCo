#! /usr/bin/env python

from config.mdf import mdf_lmf, lmf_mdf, mdf_order, VERNACULAR, ENGLISH, NATIONAL, REGIONAL
from config.tex import format_definitions
from utils.io import EOL

FRENCH = "fra"

## Functions to process some MDF fields (input)
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

mdf2lmf = dict(mdf_lmf)
mdf2lmf.update({
    "__np"  : lambda attributes, np, lexical_entry: process_np(attributes, np, lexical_entry),
    "__ec"  : lambda attributes, ec, lexical_entry: process_ec(attributes, ec, lexical_entry),
    "__sd"  : lambda attributes, sd, lexical_entry: process_sd(attributes, sd, lexical_entry),
    "__sf"  : lambda attributes, sf, lexical_entry: None,
    "__so"  : lambda attributes, so, lexical_entry: None,
    "__va"  : lambda attributes, va, lexical_entry: lexical_entry.set_variant_form(va, type="phonetics"),
    "pdf"   : lambda pdf, lexical_entry: lexical_entry.set_paradigm_form(pdf, language=FRENCH),
    "xf"    : lambda xf, lexical_entry: lexical_entry.add_example(xf, language=FRENCH),
    "xc"    : lambda xc, lexical_entry: lexical_entry.set_example_comment(xc),
    "df"    : lambda df, lexical_entry: lexical_entry.set_definition(df, language=FRENCH),
    "gf"    : lambda gf, lexical_entry: lexical_entry.set_gloss(gf, language=FRENCH)
})

lmf2mdf = dict(lmf_mdf)
lmf2mdf.update({
    "pdf": lambda paradigm: paradigm.get_paradigm(language=FRENCH),
    "xf" : lambda context: context.find_written_forms(FRENCH),
    "xc" : lambda context: context.get_comments(),
    "ec" : lambda lexical_entry: get_ec(lexical_entry),
    "sd" : lambda lexical_entry: get_sd(lexical_entry),
    "df" : lambda sense: sense.find_definitions(FRENCH),
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
order[7].insert(16, "df")
order[7][19].insert(5, "xf")
order[7][19].insert(7, "xc")
order[28].insert(5, "pdf")

## Functions to process some LaTeX fields (output)

my_font = dict({
    VERNACULAR  : lambda text: "\ipa{" + text + "}",
    ENGLISH     : lambda text: text,
    NATIONAL    : lambda text: "\zh{" + text + "}",
    REGIONAL    : lambda text: "\ipa{" + text + "}",
    FRENCH      : lambda text: text
})

def format_tone(lexical_entry, font):
    if lexical_entry.get_tones() is not None:
        result = lexical_entry.get_tones()[0]
    return result

def format_definition(lexical_entry, font, language):
    result = ""
    for sense in lexical_entry.get_senses():
        if sense.find_definitions(language) is not None:
            for definition in sense.find_definitions(language):
                result += font[language](definition)
    return result

def format_gloss(lexical_entry, font, language):
    result = ""
    for sense in lexical_entry.get_senses():
        if sense.find_glosses(language) is not None:
            for gloss in sense.find_glosses(language):
                if language == FRENCH:
                    result += "Dialecte chinois local~"
                elif language == ENGLISH:
                    result += "Local Chinese dialect"
                result +=  ": " + gloss + font[NATIONAL](u"\u3002")
    return result

def format_examples(lexical_entry, font, language):
    result = ""
    for sense in lexical_entry.get_senses():
        for context in sense.get_contexts():
            for example in context.find_written_forms(VERNACULAR):
                result += font[VERNACULAR](example) + r""" \\""" + EOL
            for example in context.find_written_forms(language):
                result += font[language](example) + r""" \\""" + EOL
            for example in context.find_written_forms(NATIONAL):
                result += font[NATIONAL](example) + r""" \\""" + EOL
    return result

def tex_fra(lexical_entry):
    """<lx> (prononciation~: <lc>~; avec le verbe copule~: <lc <type="with copula">>) TAB <ps> TAB Ton~: <np <type="tone">>.
    <df>.
    <dn>u"\u3002" Dialecte chinois local~: <gr>u"\u3002"
    <xv>
    <xf>
    <xn>
    """
    return (r"""%s (prononciation~: %s~; avec le verbe copule~: %s) \hspace{4pt} %s \hspace{4pt} Ton~: %s.""" + EOL + "%s." + EOL + "%s" + my_font[NATIONAL](u"\u3002") + "%s" + EOL + "%s" + "CL~: %s" + EOL) % \
        ("\\vspace{1cm} \\hspace{-1cm} {\Large " + my_font[VERNACULAR](lexical_entry.get_lexeme()) + "} \\hspace{0.2cm} \\hypertarget{" + unicode(lexical_entry.get_id()).replace('_', '\_') + "}{}",\
        "LC",\
        "LC AVEC COPULE",\
        "\\textcolor{teal}{\mytextsc{" + str(lexical_entry.get_partOfSpeech()) + "}}",\
        format_tone(lexical_entry, my_font),\
        format_definition(lexical_entry, my_font, language=FRENCH),\
        format_definition(lexical_entry, my_font, language=NATIONAL),\
        format_gloss(lexical_entry, my_font, language=FRENCH),\
        format_examples(lexical_entry, my_font, language=FRENCH),\
        "CL")

def tex_eng(lexical_entry):
    """<lx> (pronunciation: <lc>; with the copula verb: <lc <type="with copula">>) TAB <ps> TAB Tone: <np <type="tone">>.
    <df>.
    <dn>u"\u3002" Local Chinese dialect: <gr>u"\u3002"
    <xv>
    <xe>
    <xn>
    """
    return (r"""%s (pronunciation: %s; with the copula verb: %s) \hspace{4pt} %s \hspace{4pt} Tone: %s.""" + EOL + "%s." + EOL + "%s" + my_font[NATIONAL](u"\u3002") + "%s" + EOL + "%s" + "CL: %s" + EOL) % \
        ("\\vspace{1cm} \\hspace{-1cm} {\Large " + my_font[VERNACULAR](lexical_entry.get_lexeme()) + "} \\hspace{0.2cm} \\hypertarget{" + unicode(lexical_entry.get_id()).replace('_', '\_') + "}{}",\
        "LC",\
        "LC WITH COPULA",\
        "\\textcolor{teal}{\mytextsc{" + str(lexical_entry.get_partOfSpeech()) + "}}",\
        format_tone(lexical_entry, my_font),\
        format_definition(lexical_entry, my_font, language=ENGLISH),\
        format_definition(lexical_entry, my_font, language=NATIONAL),\
        format_gloss(lexical_entry, my_font, language=ENGLISH),\
        format_examples(lexical_entry, my_font, language=FRENCH),\
        "CL")
