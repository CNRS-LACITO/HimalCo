#! /usr/bin/env python

from config.mdf import mdf_lmf, lmf_mdf, mdf_order, ps_partOfSpeech
from config.tex import partOfSpeech_tex
from output.tex import format_definitions
from utils.io import EOL
from common.defs import VERNACULAR, ENGLISH, NATIONAL, REGIONAL

## To define languages and fonts
import config
FRENCH = "French"

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

mdf_lmf.update({
    "__np"  : lambda attributes, np, lexical_entry: process_np(attributes, np, lexical_entry),
    "__ec"  : lambda attributes, ec, lexical_entry: process_ec(attributes, ec, lexical_entry),
    "__sd"  : lambda attributes, sd, lexical_entry: process_sd(attributes, sd, lexical_entry),
    # Force first character of definitions to be in upper case
    "dv"    : lambda dv, lexical_entry: lexical_entry.set_definition(force_caps(dv), language=config.xml.vernacular),
    "de"    : lambda de, lexical_entry: lexical_entry.set_definition(force_caps(de), language=config.xml.English),
    "dn"    : lambda dn, lexical_entry: lexical_entry.set_definition(force_caps(dn), language=config.xml.national),
    "dr"    : lambda dr, lexical_entry: lexical_entry.set_definition(force_caps(dr), language=config.xml.regional),
    "df"    : lambda df, lexical_entry: lexical_entry.set_definition(force_caps(df), language=config.xml.French)
})

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

lmf_mdf.update({
    "ec" : lambda lexical_entry: get_ec(lexical_entry),
    "sd" : lambda lexical_entry: get_sd(lexical_entry),
})

## Functions to process some LaTeX fields (output)

def format_tone(lexical_entry, font):
    import output.tex as tex
    if lexical_entry.get_tones() is not None and len(lexical_entry.get_tones()) != 0:
        return tex.handle_reserved(lexical_entry.get_tones()[0])

def format_definition(lexical_entry, language_font, language):
    import output.tex as tex
    result = ""
    for sense in lexical_entry.get_senses():
        if sense.find_definitions(language) is not None:
            for definition in sense.find_definitions(language):
                result += language_font(tex.handle_fi(tex.handle_reserved(definition)))
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

def format_examples(lexical_entry, font, language_font, language):
    import output.tex as tex
    result = ""
    for sense in lexical_entry.get_senses():
        for context in sense.get_contexts():
            for example in context.find_written_forms(config.xml.vernacular):
                result += font[VERNACULAR](tex.handle_reserved(example)) + r""" \\""" + EOL
            for example in context.find_written_forms(language):
                result += language_font(tex.handle_reserved(example)) + r""" \\""" + EOL
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
    return ((r"""%s (prononciation~: %s~; avec le verbe copule~: %s) \hspace{4pt} %s \hspace{4pt} Ton~: %s.""" + EOL + "%s." + EOL + "%s" + config.xml.font[NATIONAL](u"\u3002") + "%s" + EOL + "%s" + "CL~: %s" + EOL) % \
        ("\\vspace{1cm} \\hspace{-1cm} {\Large " + config.xml.font[VERNACULAR](tex.handle_reserved(lexical_entry.get_lexeme())) + "} \\hspace{0.2cm} \\hypertarget{" + unicode(tex.handle_reserved(lexical_entry.get_id())) + "}{}",\
        "LC",\
        "LC AVEC COPULE",\
        "\\textcolor{teal}{\\textsc{" + str(lexical_entry.get_partOfSpeech()) + "}}",\
        format_tone(lexical_entry, config.xml.font),\
        format_definition(lexical_entry, config.xml.font[FRENCH], language=config.xml.French),\
        format_definition(lexical_entry, config.xml.font[NATIONAL], language=config.xml.national),\
        format_gloss(lexical_entry, config.xml.font, language=config.xml.French),\
        format_examples(lexical_entry, config.xml.font, config.xml.font[FRENCH], language=config.xml.French),\
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
    return ((r"""%s (pronunciation: %s; with the copula verb: %s) \hspace{4pt} %s \hspace{4pt} Tone: %s.""" + EOL + "%s." + EOL + "%s" + config.xml.font[NATIONAL](u"\u3002") + "%s" + EOL + "%s" + "CL: %s" + EOL) % \
        ("\\vspace{1cm} \\hspace{-1cm} {\Large " + config.xml.font[VERNACULAR](tex.handle_reserved(lexical_entry.get_lexeme())) + "} \\hspace{0.2cm} \\hypertarget{" + unicode(tex.handle_reserved(lexical_entry.get_id())) + "}{}",\
        "LC",\
        "LC WITH COPULA",\
        "\\textcolor{teal}{\\textsc{" + str(lexical_entry.get_partOfSpeech()) + "}}",\
        format_tone(lexical_entry, config.xml.font),\
        format_definition(lexical_entry, config.xml.font[ENGLISH], language=config.xml.English),\
        format_definition(lexical_entry, config.xml.font[NATIONAL], language=config.xml.national),\
        format_gloss(lexical_entry, config.xml.font, language=config.xml.English),\
        format_examples(lexical_entry, config.xml.font, config.xml.font[FRENCH], language=config.xml.French),\
        "CL")).replace("textsc", "mytextsc")
