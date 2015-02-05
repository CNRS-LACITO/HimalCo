#! /usr/bin/env python
# -*- coding: utf-8 -*-

from config.mdf import mdf_lmf, lmf_mdf, mdf_order, mdf_semanticRelation, VERNACULAR, NATIONAL, ENGLISH, REGIONAL, ps_partOfSpeech
from common.range import partOfSpeech_range
from config.tex import lmf_to_tex, partOfSpeech_tex
from utils.io import EOL
from utils.error_handling import Warning

AUDIO_PATH = "file:///Users/celine/Work/CNRS/workspace/HimalCo/dict/khaling/data/audio/"

# Consider only the first form
items=lambda lexical_entry: lexical_entry.get_citation_forms(script_name="devanagari")[0]

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
    "interj"        : "interjection",               # interjection
    "lnk"           : "coordinating conjunction",   # linker
    "n"             : "noun",                       # noun
    "Np"            : "possessed noun",             # possessed nouns
    "neg"           : "negation",                   # negative
    "num"           : "numeral",                    # number
    "prep"          : "preposition",                # preposition
    "pro"           : "pronoun",                    # pronoun/pronominal
    "vi.s"          : "stative intransitive verb",  # stative intransitive verb
    # khaling
    "vi-t"          : "bitransitive verb",          # labial verb
    "vt-i"          : "bitransitive verb",          # labial verb
    "Vi"            : "intransitive verb",          # intransitive verb
    "vt4"           : "transitive verb",            # transitive verb
    "???"           : "unknown"
})

## Possible values allowed for LMF part of speech LexicalEntry attribute
partOfSpeech_range.update([
    "unknown"
])

def check_lx(lexical_entry, lx_tmp):
    if lexical_entry.get_lexeme() != lx_tmp:
        print unicode(Warning("Lexeme '%s' generated for lexical entry '%s' is not consistant." % (lx_tmp, lexical_entry.get_lexeme())))
def check_nep(lexical_entry, nep):
    ok = False
    for form in lexical_entry.get_citation_forms(script_name="devanagari"):
        if form == nep:
            ok = True
    if not ok:
        print unicode(Warning("Citation form '%s' of lexical entry '%s' is not consistant with generated one." % (nep, lexical_entry.get_lexeme())))
def check_se(lexical_entry, se_tmp):
    ok = False
    for form in lexical_entry.find_related_forms(mdf_semanticRelation["se"]):
        if form == se_tmp:
            ok = True
    if not ok:
        print unicode(Warning("Subentry '%s' generated for lexical entry '%s' is not consistant." % (se_tmp, lexical_entry.get_lexeme())))

mdf2lmf = dict(mdf_lmf)
mdf2lmf.update({
    "nep"       : lambda nep, lexical_entry: check_nep(lexical_entry, nep), # infinitive in devanagari => check that it corresponds to 'lc_dev' value
    "wav"       : lambda wav, lexical_entry: None,
    "a"         : lambda a, lexical_entry: lexical_entry.set_spelling_variant(a),
    "se2"       : lambda se2, lexical_entry : None, # TODO
    "xv"        : lambda xv, lexical_entry: lexical_entry.create_example(xv, language=VERNACULAR, script_name="ipa"),
    # Generated markers
    "lx_dev"    : lambda lx_dev, lexical_entry : None, # root in devanagari => not used
    "lx_tmp"    : lambda lx_tmp, lexical_entry : check_lx(lexical_entry, lx_tmp), # root in IPA => check that it corresponds to 'lx' value
    "lc"        : lambda lc, lexical_entry: lexical_entry.set_citation_form(lc, script_name="ipa"), # infinitive in IPA
    "lc_dev"    : lambda lc_dev, lexical_entry : lexical_entry.set_citation_form(lc_dev, script_name="devanagari"), # infinitive in devanagari
    "se_tmp"    : lambda se_tmp, lexical_entry : check_se(lexical_entry, se_tmp), # => check that it corresponds to 'se' value
    "se2_tmp"   : lambda se2_tmp, lexical_entry : None, # TODO
    "se2_dev"   : lambda se2_dev, lexical_entry : None, # TODO
    "xv_dev"    : lambda xv_dev, lexical_entry : lexical_entry.add_example(xv_dev, language=VERNACULAR, script_name="devanagari"),
    "1s_dev"    : lambda a1s_dev, lexical_entry : None,
    "2s_dev"    : lambda a2s_dev, lexical_entry : None,
    "3s_dev"    : lambda a3s_dev, lexical_entry : None,
    "4s_dev"    : lambda a4s_dev, lexical_entry : None,
    "1d_dev"    : lambda a1d_dev, lexical_entry : None,
    "3d_dev"    : lambda a3d_dev, lexical_entry : None,
    "1p_dev"    : lambda a1p_dev, lexical_entry : None,
    "1e_dev"    : lambda a1e_dev, lexical_entry : None,
    "2p_dev"    : lambda a2p_dev, lexical_entry : None
})

lmf2mdf = dict(lmf_mdf)
lmf2mdf.update({
    "a"     : lambda lexical_entry: lexical_entry.get_spelling_variants(),
    "nep"   : lambda lexical_entry: lexical_entry.get_citation_forms(script_name="devanagari")
})

order = list(mdf_order)
order.insert(1, "a")
order.insert(2, "nep")

## Mapping between LMF part of speech LexicalEntry attribute value and LaTeX layout (output)
partOfSpeech2tex = partOfSpeech_tex
partOfSpeech2tex.update({
    "unknown" : "\\textcolor{red}{?}"
})

## Functions to process some LaTeX fields (output)

my_font = dict({
    VERNACULAR  : lambda text: "\\textbf{\ipa{" + text + "}}",
    ENGLISH     : lambda text: text,
    NATIONAL    : lambda text: "\\textit{\\skt{" + text + "}}",
    REGIONAL    : lambda text: "\ipa{" + text + "}"
})

def format_lexeme(lexical_entry, font):
    import output.tex as tex
    inf_dev = font[NATIONAL](lexical_entry.get_citation_forms(script_name="devanagari")[0]) # nep or lc_dev
    inf_api = font[VERNACULAR](lexical_entry.get_citation_forms(script_name="ipa")[0]) # lc
    root_api = font[VERNACULAR](lexical_entry.get_lexeme()) # lx
    result = "\\vspace{1cm} \\hspace{-1cm} "
    if lexical_entry.get_homonymNumber() is not None:
        # Add homonym number to lexeme
        root_api += " \\textsubscript{" + str(lexical_entry.get_homonymNumber()) + "}"
    result += inf_dev + " " + inf_api + " (" + root_api + ")"
    result += " \\hspace{0.1cm} \\hypertarget{" + tex.format_uid(lexical_entry, font) + "}{}" + EOL
    if not lexical_entry.is_subentry():
        result += "\markboth{" + inf_dev + "}{}" + EOL
    return result

def format_examples(lexical_entry, font):
    import output.tex as tex
    result = ""
    for sense in lexical_entry.get_senses():
        for context in sense.get_contexts():
            result += "\\begin{exe}" + EOL
            for example in context.find_written_forms(VERNACULAR, script_name="devanagari"): # xv_dev
                result += "\\sn " + font[NATIONAL](example) + EOL
            for example in context.find_written_forms(VERNACULAR, script_name="ipa"):
                result += "\\trans " + font[VERNACULAR](example) + EOL
            for example in context.find_written_forms(ENGLISH):
                result += "\\trans " + example + EOL
            for example in context.find_written_forms(NATIONAL):
                result += "\\trans \\textit{" + font[NATIONAL](tex.handle_font(example)) + "}" + EOL
            for example in context.find_written_forms(REGIONAL):
                result += "\\trans \\textit{[" + font[REGIONAL](example) + "]}" + EOL
            result += "\\end{exe}" + EOL
    return result

def format_paradigms(lexical_entry, font):
    result = ""
    current_label = None
    for paradigm in lexical_entry.get_paradigms():
        if paradigm.get_paradigmLabel() is not None and paradigm.get_paradigm(language=VERNACULAR) is not None:
            if paradigm.get_paradigmLabel() != current_label:
                current_label = paradigm.get_paradigmLabel()
                # Display label
                result += "\\textit{" + current_label + ":} "
            else:
                # Just add semi-colomn
                result += "; "
            result += font[VERNACULAR](paradigm.get_paradigm(language=VERNACULAR)) + " "
    return result

## Function giving order in which information must be written in LaTeX and mapping between LMF representation and LaTeX (output)
def lmf2tex(lexical_entry, font):
    import output.tex as tex
    tex_entry = ""
    # lexeme and id
    tex_entry += format_lexeme(lexical_entry, my_font)
    # TODO: phonetic variants ? or variant form ?
    # sound
    #tex_entry += tex.format_audio(lexical_entry, my_font)
    # part of speech
    tex_entry += tex.format_part_of_speech(lexical_entry, my_font, mapping=partOfSpeech2tex)
    # grammatical notes
    tex_entry += tex.format_notes(lexical_entry, my_font)
    # definition/gloss and translation
    tex_entry += tex.format_definitions(lexical_entry, my_font, languages=[VERNACULAR, ENGLISH, NATIONAL])
    # example
    tex_entry += format_examples(lexical_entry, my_font)
    # usage note
    tex_entry += tex.format_usage_notes(lexical_entry, my_font)
    # encyclopedic information
    tex_entry += tex.format_encyclopedic_informations(lexical_entry, my_font)
    # restriction
    tex_entry += tex.format_restrictions(lexical_entry, my_font)
    # synonym, antonym, morphology, related form
    tex_entry += tex.format_related_forms(lexical_entry, my_font)
    # TODO: variant form?
    tex_entry += tex.format_variant_forms(lexical_entry, my_font)
    # borrowed word
    tex_entry += tex.format_borrowed_word(lexical_entry, my_font)
    # etymology
    tex_entry += tex.format_etymology(lexical_entry, my_font)
    # paradigms
    tex_entry += tex.format_paradigms(lexical_entry, my_font)
    tex_entry += format_paradigms(lexical_entry, my_font)
    # semantic domain
    tex_entry += tex.format_semantic_domains(lexical_entry, my_font)
    # TODO? bibliography
    tex_entry += tex.format_bibliography(lexical_entry, my_font)
    # source
    tex_entry += tex.format_source(lexical_entry, my_font)
    # status
    tex_entry += tex.format_status(lexical_entry, my_font)
    # date
    tex_entry += tex.format_date(lexical_entry, my_font)
    # Handle reserved characters and fonts
    tex_entry = tex.handle_reserved(tex_entry)
    tex_entry = tex.handle_fv(tex_entry, my_font)
    tex_entry = tex.handle_fn(tex_entry, my_font)
    # Special formatting
    tex_entry = tex.handle_pinyin(tex_entry)
    tex_entry = tex.handle_caps(tex_entry)
    return tex_entry + EOL
