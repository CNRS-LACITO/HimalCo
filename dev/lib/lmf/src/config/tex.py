#! /usr/bin/env python
# -*- coding: utf-8 -*-

from config.mdf import VERNACULAR, ENGLISH, NATIONAL, REGIONAL
from utils.io import EOL

## Fonts to use in LaTeX format (output)
tex_font = dict({
    VERNACULAR  : lambda text: "\\textbf{\ipa{" + text + "}}",
    ENGLISH     : lambda text: text,
    NATIONAL    : lambda text: "\\textit{\zh{" + text + "}}",
    REGIONAL    : lambda text: "\ipa{" + text + "}"
})

## Function giving order in which information must be written in LaTeX and mapping between LMF representation and LaTeX (output)
def lmf_to_tex(lexical_entry, font=tex_font):
    """! @brief Function to convert LMF lexical entry information to be written into LaTeX commands.
    @param lexical_entry The Lexical Entry LMF instance to display.
    @return A string representing the lexical entry in LaTeX format.
    """
    import output.tex as tex
    tex_entry = ""
    # lexeme and id
    tex_entry += tex.format_lexeme(lexical_entry, font)
    # sound
    tex_entry += tex.format_audio(lexical_entry, font)
    # part of speech
    tex_entry += tex.format_part_of_speech(lexical_entry, font)
    # definition/gloss and translation
    tex_entry += tex.format_definitions(lexical_entry, font)
    # TODO
    tex_entry += tex.format_lt(lexical_entry, font)
    tex_entry += tex.format_sc(lexical_entry, font)
    tex_entry += tex.format_rf(lexical_entry, font)
    # example
    tex_entry += tex.format_examples(lexical_entry, font)
    # usage note
    tex_entry += tex.format_usage_notes(lexical_entry, font)
    # encyclopedic information
    tex_entry += tex.format_encyclopedic_informations(lexical_entry, font)
    # restriction
    tex_entry += tex.format_restrictions(lexical_entry, font)
    # TODO
    tex_entry += tex.format_lexical_functions(lexical_entry, font)
    # synonym, antonym, morphology, related form
    tex_entry += tex.format_related_forms(lexical_entry, font)
    # variant form
    tex_entry += tex.format_variant_forms(lexical_entry, font)
    # borrowed word
    tex_entry += tex.format_borrowed_word(lexical_entry, font)
    # etymology
    tex_entry += tex.format_etymology(lexical_entry, font)
    # paradigms
    tex_entry += tex.format_paradigms(lexical_entry, font)
    # TODO
    tex_entry += tex.format_table(lexical_entry, font)
    # semantic domain
    tex_entry += tex.format_semantic_domains(lexical_entry, font)
    # bibliography
    tex_entry += tex.format_bibliography(lexical_entry, font)
    # TODO
    tex_entry += tex.format_picture(lexical_entry, font)
    # notes
    tex_entry += tex.format_notes(lexical_entry, font)
    # source
    tex_entry += tex.format_source(lexical_entry, font)
    # status
    tex_entry += tex.format_status(lexical_entry, font)
    # date
    tex_entry += tex.format_date(lexical_entry, font)
    # Handle reserved characters: \ { } $ # & _ ^ ~ %
    if tex_entry.find("{") != -1:
        tex_entry = tex.format_font(tex_entry)
    if tex_entry.find("@") != -1:
        tex_entry = tex.format_pinyin(tex_entry)
    if tex_entry.find("#") != -1:
        tex_entry = tex_entry.replace('#', '\#')
    if tex_entry.find("_") != -1:
        tex_entry = tex_entry.replace('_', '\_').replace("\string\_", "\string_")
    if tex_entry.find("& ") != -1:
        tex_entry = tex_entry.replace('& ', '\& ')
    if tex_entry.find("$") != -1:
        tex_entry = tex_entry.replace('$', '')
    if tex_entry.find("^") != -1:
        tex_entry = tex_entry.replace('^', '\^')
    # Handle fonts
    if tex_entry.find("fn:") != -1:
        tex_entry = tex.format_fn(tex_entry)
    if tex_entry.find("fv:") != -1:
        tex_entry = tex.format_fv(tex_entry)
    # Special formatting
    if tex_entry.encode("utf8").find("°") != -1:
        tex_entry = tex.format_small_caps(tex_entry)
    return tex_entry + EOL
