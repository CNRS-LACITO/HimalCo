#! /usr/bin/env python
# -*- coding: utf-8 -*-

from config.mdf import mdf_lmf, lmf_mdf, mdf_semanticRelation
from utils.io import EOL
from common.defs import VERNACULAR, ENGLISH, NATIONAL, REGIONAL

## To define languages and fonts
import config
FRENCH = "French"

def get_lx(lexical_entry):
    # Do not consider special character '-' or '=' preceeding 'lx'
    return lexical_entry.get_lexeme().lstrip('-=')

items = lambda lexical_entry: get_lx(lexical_entry)

## Functions to process some MDF fields (input)

def process_lx(attributes, lx, lexical_entry):
    lexical_entry.set_lexeme(lx)
    lexical_entry.id = attributes["id"]

def process_np(attributes, np, lexical_entry):
    # <type lang>
    try:
        if attributes["type"] == "tone":
            lexical_entry.set_tone(np)
    except KeyError:
        try:
            lexical_entry.set_note(np, type="phonology", language=attributes["lang"])
        except KeyError:
            pass

def process_ec(attributes, ec, lexical_entry):
    # <lang>
    lexical_entry.set_etymology_comment(ec, attributes["lang"])

def process_sd(attributes, sd, lexical_entry):
    # <lang>
    lexical_entry.set_semantic_domain(sd, attributes["lang"])

def process_nt(attributes, nt, lexical_entry):
    # <lang type print>
    type = None
    try:
        if attributes["type"] == "comp":
            type = "comparison"
        elif attributes["type"] == "hist":
            type = "history"
        elif attributes["type"] == "sem":
            type = "semantics"
    except KeyError:
        pass
    language = None
    try:
        language = attributes["lang"]
    except KeyError:
        pass
    lexical_entry.set_note(nt, type=type, language=language)

def process_cf(attributes, cf, lexical_entry):
    # <type>
    lexical_entry.create_and_add_related_form(cf, mdf_semanticRelation[attributes["type"]])

def force_caps(text):
    """Force first letter to be in upper case.
    """
    return text[0].upper() + text[1:]

def add_final(text, language):
    """Add a final point if text has no final punctuation mark.
    """
    final_mark = set(['.', '!', '?', u"\u3002"])
    if text[-1] not in final_mark:
        if language == config.xml.English or language == config.xml.French:
            text += '.'
        elif language == config.xml.national or language == config.xml.regional:
            text += u"\u3002"
    return text

mdf_lmf.update({
    "__lx"  : lambda attributes, lx, lexical_entry: process_lx(attributes, lx, lexical_entry),
    "__se"  : lambda attributes, se, lexical_entry: lexical_entry.create_and_add_related_form(se, mdf_semanticRelation["se"]),
    "__nt"  : lambda attributes, nt, lexical_entry: process_nt(attributes, nt, lexical_entry),
    "__np"  : lambda attributes, np, lexical_entry: process_np(attributes, np, lexical_entry),
    "__ec"  : lambda attributes, ec, lexical_entry: process_ec(attributes, ec, lexical_entry),
    "__sd"  : lambda attributes, sd, lexical_entry: process_sd(attributes, sd, lexical_entry),
    "__cf"  : lambda attributes, cf, lexical_entry: process_cf(attributes, cf, lexical_entry),
    # Force first character of definitions to be in upper case
    "dv"    : lambda dv, lexical_entry: lexical_entry.set_definition(force_caps(dv), language=config.xml.vernacular),
    "de"    : lambda de, lexical_entry: lexical_entry.set_definition(add_final(force_caps(de), language=config.xml.English), language=config.xml.English),
    "dn"    : lambda dn, lexical_entry: lexical_entry.set_definition(add_final(force_caps(dn), language=config.xml.national), language=config.xml.national),
    "dr"    : lambda dr, lexical_entry: lexical_entry.set_definition(add_final(force_caps(dr), language=config.xml.regional), language=config.xml.regional),
    "df"    : lambda df, lexical_entry: lexical_entry.set_definition(add_final(force_caps(df), language=config.xml.French), language=config.xml.French)
})

## Functions to process some MDF fields (output)

def get_ec(lexical_entry):
    ec = lexical_entry.get_etymology_comment()
    if lexical_entry.get_term_source_language() is not None:
        ec = "<lang=\"" + lexical_entry.get_term_source_language() + "\">" + " " + ec
    return ec

def get_sd(lexical_entry):
    sd = ''
    sd_fr = lexical_entry.get_semantic_domains(config.xml.French)
    if sd_fr != []:
        sd += "<lang=\"fra\"> " + sd_fr[0]
    sd_en = lexical_entry.get_semantic_domains(config.xml.English)
    if sd_en != []:
        sd += EOL + "\\sd <lang=\"eng\"> " + sd_en[0]
    if sd != '':
        return sd

lmf_mdf.update({
    "ec" : lambda lexical_entry: get_ec(lexical_entry),
    "sd" : lambda lexical_entry: get_sd(lexical_entry)
})

## Functions to process some LaTeX fields (output)

def handle_tones(text):
    from utils.io import ENCODING
    import re
    result = ""
    tones = "˩˧˥".decode(encoding=ENCODING)
    # Monosyllabic
    current_pattern = "([^" + tones + "#$]+)(#?[" + tones + "]{1,2}[$#]?)([abcd123]?)"
    pattern = "^" + current_pattern + "$"
    if re.search(pattern, text):
        found = re.match(pattern, text)
        result += found.group(1) + found.group(2)
        if len(found.group(3)) != 0:
            result += "\\textsubscript{" + found.group(3) + "}"
    # Disyllabic: add a constraint on other syllables which must have at least 2 characters (maximum 5)
    syllable = "([^" + tones + "#$]{2,5})(#?[" + tones + "]{1,2}[$#]?)([abcd123]?)"
    # Handle words composed of 2, 3, 4, 5 syllables
    for syllable_nb in range (2, 6):
        current_pattern += syllable
        pattern = "^" + current_pattern + "$"
        if re.search(pattern, text):
            found = re.match(pattern, text)
            for i in range (0, syllable_nb):
                result += found.group(i*3+1) + found.group(i*3+2)
                if i != syllable_nb - 1:
                    result += found.group(i*3+3)
                elif len(found.group(i*3+3)) != 0:
                    result += "\\textsubscript{" + found.group(i*3+3) + "}"
    return result

def format_uid(lexical_entry, font):
    """Forbidden characters in filenames on Windows:
    < (less than) => none
    > (greater than) => none
    : (colon) => none
    " (double quote) => none
    / (forward slash) => none
    \ (backslash) => £
    | (vertical bar; pipe) => €
    ? (question mark) => Q
    * (asterisk) => F
    """
    import output.tex as tex
    text = tex.format_uid(lexical_entry, font)
    if text.find("|") != -1:
        text = text.replace('|', u"€")
    if text.find("?") != -1:
        text = text.replace('?', 'Q')
    if text.find("*") != -1:
        text = text.replace('*', 'F')
    return text

def format_lexeme(lexical_entry, font):
    import output.tex as tex
    result = ""
    lexeme = font[VERNACULAR](handle_tones(lexical_entry.get_lexeme()))
    if lexical_entry.is_subentry():
        result += "\\subparagraph{\\dollar\\blacksquare\\dollar "
    else:
        result += "\\paragraph{\\hspace{-0.5cm} "
    if lexical_entry.get_homonymNumber() is not None:
        # Add homonym number to lexeme
        lexeme += " \\textsubscript{" + str(lexical_entry.get_homonymNumber()) + "}"
    if lexical_entry.get_contextual_variations() is not None and len(lexical_entry.get_contextual_variations()) != 0:
        # Format contextual variations
        for var in lexical_entry.get_contextual_variations():
            result += " " + font[VERNACULAR](var)
        result += " (from: " + lexeme + ")."
    else:
        # Format lexeme
        result += "{\Large " + lexeme + "}"
    result += "} \\hypertarget{" + tex.format_uid(lexical_entry, font) + "}{}" + EOL
    if not lexical_entry.is_subentry():
        result += "\markboth{" + lexeme + "}{}" + EOL
    return result

def format_tone(lexical_entry, font):
    result = ""
    if lexical_entry.get_tones() is not None and len(lexical_entry.get_tones()) != 0:
        tone = lexical_entry.get_tones()[0]
        for c in tone:
            if c in set("abcd123"):
                result += "\\textsubscript{" + c + "}"
            else:
                result += c
    return result

def format_definition(sense, language_font, language):
    result = ""
    if sense.find_definitions(language) is not None:
        for definition in sense.find_definitions(language):
            result += language_font(definition)
    return result

def format_gloss(sense, font, language):
    result = ""
    if sense.find_glosses(config.xml.regional) is not None:
        for gloss in sense.find_glosses(config.xml.regional):
            if language == config.xml.French:
                result += "Dialecte chinois local~"
            elif language == config.xml.English:
                result += "Local Chinese dialect"
            result +=  ": " + font[REGIONAL](gloss + u"\u3002")
    # TODO : add 'gn' then 'ph' in italic
    return result

def format_etymology(lexical_entry, font, language):
    result = ""
    if lexical_entry.get_etymology() is not None:
        if language == config.xml.English:
            result += "\\textit{From:} \\textbf{" + lexical_entry.get_etymology().replace("; ", " and ") + "} "
        elif language == config.xml.French:
            result += "\\textit{De:} \\textbf{" + lexical_entry.get_etymology().replace("; ", " et ") + "} "
    # Do not display etymology comment
    #if lexical_entry.get_etymology_comment(term_source_language=language) is not None:
        #result += u"\u2018" + lexical_entry.get_etymology_comment(term_source_language=language) + u"\u2019" + ". "
    return result

def format_borrowed_word(lexical_entry, font, language):
    result = ""
    if lexical_entry.get_borrowed_word() is not None:
        if language == config.xml.French:
            result += " \\textit{De~:} "
        elif language == config.xml.English:
            result += " \\textit{From:} "
        result += lexical_entry.get_borrowed_word()
        if lexical_entry.get_written_form() is not None:
            result += " " + lexical_entry.get_written_form()
        result += ". "
    return result

def format_paradigm(lexical_entry, font, language):
    result = ""
    translation = ""
    for paradigm in lexical_entry.get_paradigms():
        if paradigm.get_paradigmLabel() == "classifier":
            if paradigm.get_language() == config.xml.vernacular:
                result += font[VERNACULAR](paradigm.get_paradigm()) + " "
            if paradigm.get_language() == language:
                translation = paradigm.get_paradigm()
                if language == config.xml.French:
                    translation = font[FRENCH](translation)
                elif language == config.xml.English:
                    translation = font[ENGLISH](translation)
    if language == config.xml.French:
        label = " \\textsc{cl}~: "
    elif language == config.xml.English:
        label = " \\textsc{cl}: "
    if result != "":
        result = label + result + translation
    return result

def format_related_forms(lexical_entry, font, language=None):
    import output.tex as tex
    result = ""
    for related_form in lexical_entry.get_related_forms(mdf_semanticRelation["sy"]):
        if language == config.xml.French:
            result += "\\textit{Syn~:} "
        else:
            result += "\\textit{Syn:} "
        if related_form.get_lexical_entry() is not None:
            result += tex.format_link(related_form.get_lexical_entry(), font)
        else:
            result += font[VERNACULAR](related_form.get_lexeme())
        result += ". "
    for related_form in lexical_entry.get_related_forms(mdf_semanticRelation["an"]):
        if language == config.xml.French:
            result += "\\textit{Ant~:} "
        else:
            result += "\\textit{Ant:} "
        if related_form.get_lexical_entry() is not None:
            result += tex.format_link(related_form.get_lexical_entry(), font)
        else:
            result += font[VERNACULAR](related_form.get_lexeme())
        result += ". "
    for morphology in lexical_entry.get_morphologies():
        if language == config.xml.French:
            result += "\\textit{Morph~:} "
        else:
            result += "\\textit{Morph:} " + font[VERNACULAR](morphology) + ". "
    for related_form in lexical_entry.get_related_forms(mdf_semanticRelation["cf"]):
        if language == config.xml.French:
            result += "\\textit{Voir~:} "
        else:
            result += "\\textit{See:} "
        if related_form.get_lexical_entry() is not None:
            result += tex.format_link(related_form.get_lexical_entry(), font)
        else:
            result += font[VERNACULAR](related_form.get_lexeme())
        result += " "
    for related_form in lexical_entry.get_related_forms(mdf_semanticRelation["hm"]):
        if language == config.xml.French:
            result += "\\textit{Voir~:} "
        else:
            result += "\\textit{See:} "
        if related_form.get_lexical_entry() is not None:
            result += tex.format_link(related_form.get_lexical_entry(), font)
        else:
            result += font[VERNACULAR](related_form.get_lexeme())
        result += " "
    return result

def format_senses(lexical_entry, font, language):
    import output.tex as tex
    result = ""
    if language == config.xml.French:
        language_font = config.xml.font[FRENCH]
    elif language == config.xml.English:
        language_font = config.xml.font[ENGLISH]
    # Order by sense number
    senses = lexical_entry.get_senses()
    senses.sort(key=lambda sense: sense.get_senseNumber(integer=True))
    for sense in senses:
        if sense.get_senseNumber() is not None:
            result += sense.get_senseNumber() + ") "
        result += format_definition(sense, language_font, language=language) + EOL
        result += format_definition(sense, config.xml.font[NATIONAL], language=config.xml.national)
        result += format_gloss(sense, config.xml.font, language=language) + EOL
        result += tex.format_examples(sense, config.xml.font, languages=[config.xml.vernacular, language, config.xml.national])
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
    tex_entry = ""
    # Do not display lexical entry if lexeme is '???'
    if lexical_entry.get_lexeme() == "???":
        return tex_entry
    tex_entry = (r"""%s%s %s %s \hspace{4pt} Ton~: %s.""" + EOL + "%s%s%s%s%s" + EOL) % \
        (format_lexeme(lexical_entry, config.xml.font),\
        tex.format_audio(lexical_entry, font).replace('$', "\\dollar"),\
        "\\textcolor{red}{UID=" + format_uid(lexical_entry, font) + "}",\
        "\\textcolor{teal}{\\textsc{" + str(lexical_entry.get_partOfSpeech()) + "}}",\
        format_tone(lexical_entry, config.xml.font),\
        format_etymology(lexical_entry, font=config.xml.font, language=config.xml.French),\
        format_borrowed_word(lexical_entry, font=config.xml.font, language=config.xml.French),\
        format_senses(lexical_entry, font, language=config.xml.French),
        format_paradigm(lexical_entry, font=config.xml.font, language=config.xml.French),\
        format_related_forms(lexical_entry, font, language=config.xml.French))
    # Special formatting
    tex_entry = tex.handle_caps(tex_entry).replace("textsc", "mytextsc")
    # Handle reserved characters and fonts
    tex_entry = tex.handle_reserved(tex_entry)
    tex_entry = tex.handle_quotes(tex_entry)
    tex_entry = tex.handle_fv(tex_entry, config.xml.font)
    tex_entry = tex.handle_fn(tex_entry, config.xml.font)
    return tex_entry

def tex_eng(lexical_entry, font):
    """<lx> (pronunciation: <lc>; with the copula verb: <lc <type="with copula">>) TAB <ps> TAB Tone: <np <type="tone">>.
    <df>.
    <dn>u"\u3002" Local Chinese dialect: <gr>u"\u3002"
    <xv>
    <xe>
    <xn>
    """
    import output.tex as tex
    tex_entry = ""
    # Do not display lexical entry if lexeme is '???'
    if lexical_entry.get_lexeme() == "???":
        return tex_entry
    tex_entry = (r"""%s%s %s %s \hspace{4pt} Tone: %s.""" + EOL + "%s%s%s%s%s" + EOL) % \
        (format_lexeme(lexical_entry, config.xml.font),\
        tex.format_audio(lexical_entry, font).replace('$', "\\dollar"),\
        "\\textcolor{red}{UID=" + format_uid(lexical_entry, font) + "}",\
        "\\textcolor{teal}{\\textsc{" + str(lexical_entry.get_partOfSpeech()) + "}}",\
        format_tone(lexical_entry, config.xml.font),\
        format_etymology(lexical_entry, font=config.xml.font, language=config.xml.English),\
        format_borrowed_word(lexical_entry, font=config.xml.font, language=config.xml.English),\
        format_senses(lexical_entry, font, language=config.xml.English),\
        format_paradigm(lexical_entry, font=config.xml.font, language=config.xml.English),\
        format_related_forms(lexical_entry, font, language=config.xml.English))
    # Special formatting
    tex_entry = tex.handle_caps(tex_entry).replace("textsc", "mytextsc")
    # Handle reserved characters and fonts
    tex_entry = tex.handle_reserved(tex_entry)
    tex_entry = tex.handle_quotes(tex_entry)
    tex_entry = tex.handle_fv(tex_entry, font)
    tex_entry = tex.handle_fn(tex_entry, font)
    return tex_entry
