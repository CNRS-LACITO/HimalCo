#! /usr/bin/env python
# -*- coding: utf-8 -*-

from pylmflib.config.mdf import mdf_lmf, lmf_mdf, mdf_semanticRelation
from pylmflib.config.tex import partOfSpeech_tex
from pylmflib.utils.io import EOL, ENCODING
from pylmflib.common.defs import VERNACULAR, ENGLISH, NATIONAL, REGIONAL
from pylmflib.utils.error_handling import Warning

## To define languages and fonts
import pylmflib.config
FRENCH = "French"

# To access options
from pylmflib import options
global options

def get_lx(lexical_entry):
    # Do not consider special characters '~', '‑', '-', '=', '*' nor '|' separation
    return lexical_entry.get_lexeme().lstrip('*').replace('=', '').replace('-', '').replace('‑'.decode(encoding=ENCODING), '').replace('~', '').replace(" | ", '')

items = lambda lexical_entry: get_lx(lexical_entry)
condition = lambda lexical_entry: lexical_entry.get_lexeme() != "???" and lexical_entry.get_lexeme() != "xxxx" and lexical_entry.get_lexeme() != "*"

def classify_lexicon(lexicon, sort_order, sort_type):
    import re
    initials = ""
    rimes = ""
    tones = ""
    for str, rank in sort_order.iteritems():
        if "initial" in sort_type[str]:
            initials += str
        if "rime" in sort_type[str]:
            rimes += str
        if "tone" in sort_type[str]:
            tones += str
    def compare_lx(x, y):
        unknown = set(["xxxx", "???", ""])
        cmp_x = x
        cmp_y = y
        pattern = "^([" + initials.replace('j', '').replace('w', '') + "]{0,3})([" + rimes + "]{1,2})#?([" + tones + "]{0,2})[$#]?[123]?(.*)$"
        n = 5
        while(n > 0):
            initial_x = ""
            rime_x = ""
            tone_x = ""
            initial_y = ""
            rime_y = ""
            tone_y = ""
            char_x = []
            char_y = []
            found = re.match(pattern, cmp_x)
            if found is None:
                if len(cmp_x) == 1:
                    if cmp_x in initials:
                        initial_x = cmp_x
                        rime_x = ""
                    elif cmp_x in rimes:
                        initial_x = ""
                        rime_x = cmp_x
                    tone_x = ""
                    cmp_x = ""
                else:
                    if cmp_x not in unknown:
                        print Warning("Cannot sort " + cmp_x.encode(ENCODING))
                    return 1
            else:
                initial_x = found.group(1)
                rime_x = found.group(2)
                tone_x = found.group(3)
                cmp_x = found.group(4)
                # Before comparing, handle combining tilde of 'ɻ̃' if any
                if rime_x == u"\u0303":
                    initial_x += rime_x
                    rime_x = ""
            found = re.match(pattern, cmp_y)
            if found is None:
                if len(cmp_y) == 1:
                    if cmp_y in initials:
                        initial_y = cmp_y
                        rime_y = ""
                    elif cmp_y in rimes:
                        initial_y = ""
                        rime_y = cmp_y
                    tone_y = ""
                    cmp_y = ""
                else:
                    if cmp_y not in unknown:
                        print Warning("Cannot sort " + cmp_y.encode(ENCODING))
                    return -1
            else:
                initial_y = found.group(1)
                rime_y = found.group(2)
                tone_y = found.group(3)
                cmp_y = found.group(4)
                # Before comparing, handle combining tilde of 'ɻ̃' if any
                if rime_y == u"\u0303":
                    initial_y += rime_y
                    rime_y = ""
            if len(initial_x) != 0:
                char_x.append(initial_x)
            if len(rime_x) != 0:
                char_x.append(rime_x)
            if len(initial_y) != 0:
                char_y.append(initial_y)
            if len(rime_y) != 0:
                char_y.append(rime_y)
            try:
                try:
                    char_x[0]
                except IndexError:
                    return -1
                try:
                    char_y[0]
                except IndexError:
                    return 1
                # If the 1st one is lower than the 2nd one, its rank is decremented
                if sort_order[char_x[0]] < sort_order[char_y[0]]:
                    return -1
                # If the 1st one is greater than the 2nd one, its rank is incremented
                elif sort_order[char_x[0]] > sort_order[char_y[0]]:
                    return 1
                else: # sort_order[char_x[0]] == sort_order[char_y[0]]
                    single = False
                    try:
                        char_x[1]
                    except IndexError:
                        single = True
                    try:
                        char_y[1]
                    except IndexError:
                        single = True
                    if not single:
                        # If the 1st one is lower than the 2nd one, its rank is decremented
                        if sort_order[char_x[1]] < sort_order[char_y[1]]:
                            return -1
                        # If the 1st one is greater than the 2nd one, its rank is incremented
                        elif sort_order[char_x[1]] > sort_order[char_y[1]]:
                            return 1
                    # sort_order[char_x[1]] == sort_order[char_y[1]]
                    # If the 1st one is lower than the 2nd one, its rank is decremented
                    if sort_order[tone_x] < sort_order[tone_y]:
                        return -1
                    # If the 1st one is greater than the 2nd one, its rank is incremented
                    elif sort_order[tone_x] > sort_order[tone_y]:
                        return 1
                    else: # sort_order[tone_x] == sort_order[tone_y]
                        if cmp_x == "":
                            return -1
                        if cmp_y == "":
                            return 1
                        n -= 1
                        if n == 0:
                            # If all characters match, both equal => do nothing
                            return 0
            except KeyError:
                print Warning("Cannot compare " + x.encode(ENCODING) + " and " + y.encode(ENCODING))
                return 0
    lexicon.sort_lexical_entries(items=items, sort_order=sort_order, comparison=compare_lx)
    lexicon.sort_homonym_numbers(condition=condition)

## Functions to process some MDF fields (input)

def process_lx(attributes, lx, lexical_entry):
    lexical_entry.set_lexeme(lx)
    # UID is already set
    #lexical_entry.id = attributes["id"]

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
        if language == pylmflib.config.xml.English or language == pylmflib.config.xml.French:
            text += '.'
        elif language == pylmflib.config.xml.national or language == pylmflib.config.xml.regional:
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
    "dv"    : lambda dv, lexical_entry: lexical_entry.set_definition(force_caps(dv), language=pylmflib.config.xml.vernacular),
    "de"    : lambda de, lexical_entry: lexical_entry.set_definition(add_final(force_caps(de), language=pylmflib.config.xml.English), language=pylmflib.config.xml.English),
    "dn"    : lambda dn, lexical_entry: lexical_entry.set_definition(add_final(force_caps(dn), language=pylmflib.config.xml.national), language=pylmflib.config.xml.national),
    "dr"    : lambda dr, lexical_entry: lexical_entry.set_definition(add_final(force_caps(dr), language=pylmflib.config.xml.regional), language=pylmflib.config.xml.regional),
    "df"    : lambda df, lexical_entry: lexical_entry.set_definition(add_final(force_caps(df), language=pylmflib.config.xml.French), language=pylmflib.config.xml.French)
})

## Functions to process some MDF fields (output)

def get_ec(lexical_entry):
    ec = lexical_entry.get_etymology_comment()
    if lexical_entry.get_term_source_language() is not None:
        ec = "<lang=\"" + lexical_entry.get_term_source_language() + "\">" + " " + ec
    return ec

def get_sd(lexical_entry):
    sd = ''
    sd_fr = lexical_entry.get_semantic_domains(pylmflib.config.xml.French)
    if sd_fr != []:
        sd += "<lang=\"fra\"> " + sd_fr[0]
    sd_en = lexical_entry.get_semantic_domains(pylmflib.config.xml.English)
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
    from pylmflib.utils.io import ENCODING
    import re
    result = ""
    tones = "˩˧˥".decode(encoding=ENCODING)
    # Monosyllabic
    current_pattern = "([^" + tones + "#$]+)(#?[" + tones + "]{0,2}[$#-]?)([abcd123]?)"
    pattern = "^" + current_pattern + "$"
    if re.search(pattern, text):
        found = re.match(pattern, text)
        result += found.group(1) + found.group(2)
        if len(found.group(3)) != 0:
            result += "\\textsubscript{" + found.group(3) + "}"
        return result
    # Disyllabic: add a constraint on other syllables which must have at least 1 character (maximum 5)
    syllable = "([^" + tones + "#$]{1,5})(#?[" + tones + "]{1,2}[$#]?)([abcd123]?)"
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
        else:
            return text
    return result

def handle_tilde(text):
    return text.replace('~', "\\textasciitilde{}")

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
    import pylmflib.output.tex as tex
    text = ""
    if options.uid:
        text = tex.format_uid(lexical_entry, font)
        if text.find("|") != -1:
            text = text.replace('|', u"€")
        if text.find("?") != -1:
            text = text.replace('?', 'Q')
        if text.find("*") != -1:
            text = text.replace('*', 'F')
        text = " \\textcolor{red}{UID=" + text + "} "
    return text

def format_lexeme(lexical_entry, font):
    import pylmflib.output.tex as tex
    result = ""
    lexeme = font[VERNACULAR](handle_tilde(handle_tones(lexical_entry.get_lexeme())))
    surface_form = font[VERNACULAR](handle_tilde(handle_tones(lexical_entry.get_citation_forms()[0])))
    if lexical_entry.is_subentry():
        result += "\\paragraph{\\dollar\\blacksquare\\dollar "
    else:
        result += "\\subsection{\\hspace{-0.5cm} "
    if lexical_entry.get_homonymNumber() is not None:
        # Add homonym number to lexeme
        lexeme += " \\textsubscript{" + str(lexical_entry.get_homonymNumber()) + "}"
    if lexical_entry.get_contextual_variations() is not None and len(lexical_entry.get_contextual_variations()) != 0:
        # Format contextual variations
        for var in lexical_entry.get_contextual_variations():
            result += " " + font[VERNACULAR](handle_tilde(var))
        result += " (from: " + lexeme + ")."
    else:
        # Format lexeme
        result += "{\Large " + lexeme + "}\\hspace{0.5cm}"
        result += "[\kern2pt{" + surface_form + "}\kern2pt]"
    result += "} \\hypertarget{" + tex.format_uid(lexical_entry, font) + "}{}" + EOL
    if not lexical_entry.is_subentry():
        result += "\markboth{" + lexeme + "}{}" + EOL
    return result

def format_link(lexical_entry, font):
    """! @brief Display hyperlink to a lexical entry in LaTeX format.
    @param lexical_entry The targeted Lexical Entry LMF instance.
    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.
    @return A string representing the hyperlink in LaTeX format.
    """
    result = "\\hyperlink{" + format_uid(lexical_entry, font) + "}{" + font[VERNACULAR](handle_tilde(handle_tones(lexical_entry.get_lexeme())))
    if lexical_entry.get_homonymNumber() is not None:
        result += " \\textsubscript{" + str(lexical_entry.get_homonymNumber()) + "}"
    result += "}"
    return result

def format_tone(lexical_entry, font):
    result = ""
    if lexical_entry.get_tones() is not None and len(lexical_entry.get_tones()) != 0:
        tone = lexical_entry.get_tones()[0]
        # Subscript tone sub-categories only if they follow L, M, or H character
        prev = None
        for c in tone:
            if c in set("abcd123") and prev in set("LMH"):
                result += "\\textsubscript{" + c + "}"
            else:
                result += c
            prev = c
    return result

def format_usage_notes(sense, font, language_font, language):
    result = ""
    for usage in sense.find_usage_notes(language=language):
        result += "\\textit{" + force_caps(language_font(usage)) + "}"
    for usage in sense.find_usage_notes(language=pylmflib.config.xml.national):
        result += " [" + font[NATIONAL](usage) + "] "
    return result

def format_definition(sense, language_font, language):
    result = ""
    if sense.find_definitions(language) is not None:
        for definition in sense.find_definitions(language):
            result += language_font(definition) + " "
    return result

def format_gloss(sense, font, language):
    result = ""
    if sense.find_glosses(pylmflib.config.xml.regional) is not None:
        for gloss in sense.find_glosses(pylmflib.config.xml.regional):
            if language == pylmflib.config.xml.French:
                result += "Dialecte chinois local~:"
            elif language == pylmflib.config.xml.English:
                result += "Local Chinese dialect:"
            elif language == pylmflib.config.xml.national:
                result += u"\\zh{当地汉语方言：}"
            result += font[REGIONAL](gloss + u"\u3002")
    # TODO : add 'gn' then 'ph' in italic
    return result

def format_examples(sense, font, languages=None):
    import pylmflib.output.tex as tex
    result = ""
    if languages is None:
        languages = [pylmflib.config.xml.vernacular, pylmflib.config.xml.English, pylmflib.config.xml.national, pylmflib.config.xml.regional]
    for context in sense.get_contexts():
        ref = ""
        if context.get_speakerID() is not None and context.get_speakerID() != "F4":
            ref = "[" + context.get_speakerID() + "] "
        tmp = u"¶ "
        for language in languages:
            for example in context.find_written_forms(language):
                if language == pylmflib.config.xml.vernacular:
                    tmp += font[VERNACULAR](handle_tilde(ref + example)) + " "
                elif language == pylmflib.config.xml.national:
                    tmp += "" + font[NATIONAL](tex.handle_font(example)) + " "
                elif language == pylmflib.config.xml.regional:
                    tmp += "\\textit{[" + font[REGIONAL](example) + "]}" + " "
                elif language == pylmflib.config.xml.French:
                    tmp += "\\textcolor{PineGreen}{\selectlanguage{french}" + example + "} "
                else:  # language == pylmflib.config.xml.English:
                    tmp += "\\textcolor{Sepia}{\selectlanguage{english}" + example + "} "
        # LaTeX does not support empty examples
        if len(tmp) != 0:

            result += " " + tmp + " " + EOL
    return result

def format_etymology(lexical_entry, font, language):
    result = ""
    if lexical_entry.get_etymology() is not None:
        if language == pylmflib.config.xml.English:
            result += "\\textit{From:} \\textbf{" + lexical_entry.get_etymology().replace("; ", " and ") + "} "
        elif language == pylmflib.config.xml.French:
            result += "\\textit{De:} \\textbf{" + lexical_entry.get_etymology().replace("; ", " et ") + "} "
    # Do not display etymology comment
    #if lexical_entry.get_etymology_comment(term_source_language=language) is not None:
        #result += u"\u2018" + lexical_entry.get_etymology_comment(term_source_language=language) + u"\u2019" + ". "
    return result

def format_borrowed_word(sense, font, language):
    result = ""
    lang = sense.get_borrowed_word()
    if lang is not None:
        if language == pylmflib.config.xml.French:
            result += " Emprunt~: "
            # Translate languages names for French version
            lang = lang.replace(u"Chinese", u"chinois").replace(u"Tibetan", u"tibétain").lower()
        elif language == pylmflib.config.xml.English:
            result += " Borrowing: "
        elif language == pylmflib.config.xml.national:
            result += u" \\zh{【借词】}"
            lang = lang.replace(u"Chinese", "").replace(u"Tibetan", u"\\zh{藏语}")
        result += lang
        if sense.get_written_form() is not None:
            if language == pylmflib.config.xml.national:
                result += sense.get_written_form()  # Pour ne plus avoir d'espace superflu.
            else:
                result += " " + sense.get_written_form()
        result += EOL
    return result

def format_paradigm(sense, font, language):
    result = ""
    translation = ""
    for paradigm in sense.get_paradigms():
        if paradigm.get_paradigmLabel() == "classifier":
            if paradigm.get_language() == pylmflib.config.xml.vernacular:
                result += font[VERNACULAR](handle_tilde(paradigm.get_paradigm())) + " "
            if paradigm.get_language() == language:
                translation = paradigm.get_paradigm()
                if language == pylmflib.config.xml.French:
                    translation = font[FRENCH](translation)
                elif language == pylmflib.config.xml.English:
                    translation = font[ENGLISH](translation)
                elif language == pylmflib.config.xml.national:
                    translation = font[NATIONAL](translation)
    if language == pylmflib.config.xml.French:
        label = " \\textsc{clf}~: "
    elif language == pylmflib.config.xml.English:
        label = " \\textsc{clf}: "
    elif language == pylmflib.config.xml.national:
        label = u" \\zh{量词}: "
    if result != "":
        result = label + result + translation
    return result

def format_related_forms(lexical_entry, font, language=None):
    import pylmflib.output.tex as tex
    result = ""
    for related_form in lexical_entry.get_related_forms(mdf_semanticRelation["sy"]):
        if language == pylmflib.config.xml.French:
            result += "\\textit{Syn~:} "
        elif language == pylmflib.config.xml.national:
            result += u"\\zh{~【同义词】~} "
        else:
            result += "\\textit{Syn:} "
        if related_form.get_lexical_entry() is not None:
            result += format_link(related_form.get_lexical_entry(), font)
        else:
            result += font[VERNACULAR](handle_tilde(related_form.get_lexeme()))
        result += ". "
    for related_form in lexical_entry.get_related_forms(mdf_semanticRelation["an"]):
        if language == pylmflib.config.xml.French:
            result += "\\textit{Ant~:} "
        elif language == pylmflib.config.xml.national:
            result += u"\\zh{~【反义词】~} "
        else:
            result += "\\textit{Ant:} "
        if related_form.get_lexical_entry() is not None:
            result += format_link(related_form.get_lexical_entry(), font)
        else:
            result += font[VERNACULAR](handle_tilde(related_form.get_lexeme()))
        result += ". "
    for morphology in lexical_entry.get_morphologies():
        if language == pylmflib.config.xml.French:
            result += "\\textit{Morph~:} "
        else:
            result += "\\textit{Morph:} " + font[VERNACULAR](handle_tilde(morphology)) + ". "
    for related_form in lexical_entry.get_related_forms(mdf_semanticRelation["cf"]):
        if language == pylmflib.config.xml.French:
            result += "\\textit{Voir~:} "
        elif language == pylmflib.config.xml.national:
            result += u"\\zh{~【参考】~} "
        else:
            result += "\\textit{See:} "
        if related_form.get_lexical_entry() is not None:
            result += format_link(related_form.get_lexical_entry(), font)
        else:
            result += font[VERNACULAR](handle_tilde(related_form.get_lexeme()))
        result += " "
    for related_form in lexical_entry.get_related_forms(mdf_semanticRelation["hm"]):
        if language == pylmflib.config.xml.French:
            result += "\\textit{Voir~:} "
        elif language == pylmflib.config.xml.national:
            result += u"\\zh{~【同音词】~} "
        else:
            result += "\\textit{See:} "
        if related_form.get_lexical_entry() is not None:
            result += format_link(related_form.get_lexical_entry(), font)
        else:
            result += font[VERNACULAR](handle_tilde(related_form.get_lexeme()))
        result += " "
    return result

def format_senses(lexical_entry, font, language, definition_languages=[]):
    import pylmflib.output.tex as tex
    result = ""
    if language == pylmflib.config.xml.French:
        language_font = font[FRENCH]
    elif language == pylmflib.config.xml.English:
        language_font = font[ENGLISH]
    elif language == pylmflib.config.xml.national:
        language_font = font[NATIONAL]
    # Order by sense number
    senses = lexical_entry.get_senses()
    senses.sort(key=lambda sense: sense.get_senseNumber(integer=True))
    for sense in senses:
        if sense.get_senseNumber() is not None:
            # In LaTeX, "\ding{202}" represents '➊' character, "\ding{203}" '➋' character, etc.
            code = 201 + int(sense.get_senseNumber())
            result += "\ding{" + str(code) + "} "
        result += format_usage_notes(sense, font, language_font, language=language)
        for definition_language in definition_languages:
            language_font = font[FRENCH] if definition_language == pylmflib.config.xml.French else font[ENGLISH] if definition_language == pylmflib.config.xml.English else font[NATIONAL]
            result += format_definition(sense, language_font, language=definition_language)
        result += format_gloss(sense, font, language=language)
        result += format_borrowed_word(sense, font, language=language)
        result += format_examples(sense, font, languages=[pylmflib.config.xml.vernacular] + definition_languages)
        result += format_paradigm(sense, font=pylmflib.config.xml.font, language=pylmflib.config.xml.national)
    return result

def format_part_of_speech(lexical_entry, language):
    result = ""
    part_of_speech = "-"

    if lexical_entry.get_partOfSpeech() is not None:
        part_of_speech = partOfSpeech_tex[(language, lexical_entry.get_partOfSpeech())]

    # LaTeX command 'mytextsc' does not support spaces
    for part in part_of_speech.split():
        if language == pylmflib.config.xml.national:
            result += "\\textcolor{teal}{\\zh{" + part + "}} "
        else:
            result += "\\textcolor{teal}{\\textsc{" + part + "}} "
    return result

def tex_fra(lexical_entry, font):
    """<lx> (prononciation~: <lc>~; avec le verbe copule~: <lc <type="with copula">>) TAB <ps> TAB Ton~: <np <type="tone">>.
    <df>.
    <dn>u"\u3002" Dialecte chinois local~: <gr>u"\u3002"
    <xv>
    <xf>
    <xn>
    """
    import pylmflib.output.tex as tex
    tex_entry = ""
    # Do not display lexical entry if lexeme is '???' or '*'
    if lexical_entry.get_lexeme() == "???" or lexical_entry.get_lexeme() == "*":
        return tex_entry
    tex_entry = (r"""%s%s%s%s\hspace{4pt} Ton~: %s.""" + EOL + "%s%s%s%s" + EOL) % \
        (format_lexeme(lexical_entry, pylmflib.config.xml.font),\
        tex.format_audio(lexical_entry, font).replace('$', "\\dollar"),\
        format_uid(lexical_entry, font),\
        format_part_of_speech(lexical_entry, pylmflib.config.xml.French),\
        format_tone(lexical_entry, pylmflib.config.xml.font),\
        format_etymology(lexical_entry, font=pylmflib.config.xml.font, language=pylmflib.config.xml.French),\
        format_senses(lexical_entry, font, language=pylmflib.config.xml.French, definition_languages=[pylmflib.config.xml.French, pylmflib.config.xml.national]),
        format_paradigm(lexical_entry, font=pylmflib.config.xml.font, language=pylmflib.config.xml.French),\
        format_related_forms(lexical_entry, font, language=pylmflib.config.xml.French))
    # Special formatting
    tex_entry = tex.handle_caps(tex_entry).replace("textsc", "mytextsc")
    # Handle reserved characters and fonts
    tex_entry = tex.handle_reserved(tex_entry)
    tex_entry = tex.handle_quotes(tex_entry)
    tex_entry = tex.handle_fv(tex_entry, font)
    tex_entry = tex.handle_fn(tex_entry, font)
    tex_entry = tex.handle_fi(tex_entry)
    return tex_entry

def tex_eng(lexical_entry, font):
    """<lx> (pronunciation: <lc>; with the copula verb: <lc <type="with copula">>) TAB <ps> TAB Tone: <np <type="tone">>.
    <df>.
    <dn>u"\u3002" Local Chinese dialect: <gr>u"\u3002"
    <xv>
    <xe>
    <xn>
    """
    import pylmflib.output.tex as tex
    tex_entry = ""
    # Do not display lexical entry if lexeme is '???' or '*'
    if lexical_entry.get_lexeme() == "???" or lexical_entry.get_lexeme() == "*":
        return tex_entry
    tex_entry = (r"""%s%s%s%s\hspace{4pt} Tone: %s.""" + EOL + "%s%s%s%s" + EOL) % \
        (format_lexeme(lexical_entry, pylmflib.config.xml.font),\
        tex.format_audio(lexical_entry, font).replace('$', "\\dollar"),\
        format_uid(lexical_entry, font),\
        format_part_of_speech(lexical_entry, pylmflib.config.xml.English),\
        format_tone(lexical_entry, pylmflib.config.xml.font),\
        format_etymology(lexical_entry, font=pylmflib.config.xml.font, language=pylmflib.config.xml.English),\
        format_senses(lexical_entry, font, language=pylmflib.config.xml.English, definition_languages=[pylmflib.config.xml.English, pylmflib.config.xml.national]),\
        format_paradigm(lexical_entry, font=pylmflib.config.xml.font, language=pylmflib.config.xml.English),\
        format_related_forms(lexical_entry, font, language=pylmflib.config.xml.English))
    # Special formatting
    tex_entry = tex.handle_caps(tex_entry).replace("textsc", "mytextsc")
    # Handle reserved characters and fonts
    tex_entry = tex.handle_reserved(tex_entry)
    tex_entry = tex.handle_quotes(tex_entry)
    tex_entry = tex.handle_fv(tex_entry, font)
    tex_entry = tex.handle_fn(tex_entry, font)
    tex_entry = tex.handle_fi(tex_entry)
    return tex_entry

def tex_cmn(lexical_entry, font):
    """<lx> (pronunciation: <lc>; with the copula verb: <lc <type="with copula">>) TAB <ps> TAB Tone: <np <type="tone">>.
    <df>.
    <dn>u"\u3002"当地汉语方言： <gr>u"\u3002"
    <xv>
    <xe>
    <xn>
    """
    import pylmflib.output.tex as tex

    tex_entry = ""
    # Do not display lexical entry if lexeme is '???' or '*'
    if lexical_entry.get_lexeme() == "???" or lexical_entry.get_lexeme() == "*":  
        return tex_entry
    arg1 = format_lexeme(lexical_entry, pylmflib.config.xml.font)
    arg2 = tex.format_audio(lexical_entry, font).replace('$', "\\dollar")
    arg3 = format_uid(lexical_entry, font)
    arg4 = format_part_of_speech(lexical_entry, pylmflib.config.xml.national)
    arg5 = format_tone(lexical_entry, pylmflib.config.xml.font)
    arg6 = format_etymology(lexical_entry, font=pylmflib.config.xml.font, language=pylmflib.config.xml.national)
    arg7 = format_senses(lexical_entry, font=pylmflib.config.xml.font, language=pylmflib.config.xml.national, definition_languages=[pylmflib.config.xml.national, pylmflib.config.xml.English, pylmflib.config.xml.French])
    arg8 = format_related_forms(lexical_entry, font, language=pylmflib.config.xml.national)

    tex_entry = (u"""%s%s%s%s\hspace{4pt} \zh{声调类：} %s.""" + EOL + "%s%s%s" + EOL) %  (arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8)
    # Special formatting
    tex_entry = tex.handle_caps(tex_entry).replace("textsc", "mytextsc")
    # Handle reserved characters and fonts
    tex_entry = tex.handle_reserved(tex_entry)
    tex_entry = tex.handle_quotes(tex_entry)
    tex_entry = tex.handle_fv(tex_entry, font)
    tex_entry = tex.handle_fn(tex_entry, font)
    tex_entry = tex.handle_fi(tex_entry)
    return tex_entry
