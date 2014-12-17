#! /usr/bin/env python
# -*- coding: utf-8 -*-

from config.tex import lmf_to_tex
from config.mdf import VERNACULAR, ENGLISH, NATIONAL, REGIONAL, mdf_semanticRelation, pd_grammaticalNumber, pd_person, pd_anymacy, pd_clusivity
from utils.io import open_read, open_write, EOL
from utils.error_handling import OutputError, Warning

def compute_header(preamble):
    """! @brief Create LaTeX header.
    @param preamble The name of the LaTeX file with full path containing the LaTeX header of the document, for instance 'user/config/japhug.tex'.
    @return A Python string containing read information.
    """
    header = ""
    if preamble is not None:
        hdr = open_read(preamble)
        header = hdr.read()
        hdr.close()
    return header

def tex_write(object, filename, preamble=None, lmf2tex=lmf_to_tex):
    """! @brief Write a LaTeX file.
    @param object The LMF instance to convert into LaTeX output format.
    @param filename The name of the LaTeX file to write with full path, for instance 'user/output.tex'.
    @param preamble The name of the LaTeX file with full path containing the LaTeX header of the document, for instance 'user/config/japhug.tex'. Deafult value is None.
    @param lmf2tex A function giving the mapping from LMF representation information that must be written to LaTeX commands, in a defined order. Default value is 'lmf_to_tex' function defined in 'src/config/tex.py'. Please refer to it as an example.
    """
    tex_file = open_write(filename)
    # Add file header if any
    tex_file.write(compute_header(preamble))
    # Insert LaTeX commands to create a document
    tex_file.write(EOL + "\\begin{document}" + EOL)
    tex_file.write("\\maketitle" + EOL)
    tex_file.write("\\newpage" + EOL)
    tex_file.write("\\begin{multicols}{2}" + EOL * 2)
    # For each element to write, get the corresponding LMF value
    if object.__class__.__name__ == "LexicalResource":
        for lexicon in object.get_lexicons():
            for lexical_entry in lexicon.get_lexical_entries():
                # Consider only main entries (subentries will be written as parts of the main entry)
                if lexical_entry.find_related_forms("main entry") == []:
                    tex_file.write(lmf2tex(lexical_entry))
                    # Separate lexical entries from each others with a blank line
                    tex_file.write(EOL)
                    # Handle subentries
                    for related_form in lexical_entry.get_related_forms("subentry"):
                        if related_form.get_lexical_entry() is not None:
                            tex_file.write(lmf2tex(related_form.get_lexical_entry()))
                            # Separate sub-entries from each others with a blank line
                            tex_file.write(EOL)
    else:
        raise OutputError(object, "Object to write must be a Lexical Resource.")
    # Insert LaTeX commands to finish the document properly
    tex_file.write("\end{multicols}" + EOL)
    tex_file.write("\end{document}" + EOL)
    tex_file.close()

## Functions to process LaTeX fields (output)

def format_font(text):
    """Replace '\{xxx}' by '\ipa{xxx}'.
    """
    return text.replace("\\{", "\\ipa{")

def format_fn(text):
    """Replace 'fn:xxx' by '\\textcolor{brown}{\zh{xxx}}'.
    """
    import re
    return re.sub(r"(\w*)fn:([^\s\.,)]*)(\w*)", r"\1" + r"\\textcolor{brown}{\zh{" + r"\2" + "}}" + r"\3", text)

def format_fv(text):
    """Replace 'fv:xxx' by '\textcolor{blue}{\textbf{\ipa{xxx}}}'.
    """
    import re
    pattern = r"(.*[ }])?fv:([^\s\.,)]*)(.*)"
    s = re.match(pattern, text)
    if not s:
        return text
    while s:
        result = ''
        if s.group(1) is not None:
            result += s.group(1)
        result += r"\textcolor{blue}{\textbf{\ipa{" + s.group(2) + "}}}" + s.group(3)
        text = result
        s = re.match(pattern, text)
    return result

def format_small_caps(text):
    """Replace '°xxx' by '\textsc{xxx}' in translated examples.
    """
    import re
    return re.sub(r"(\w*)°([^\s\.,)+/:]*)(\w*)", r"\1" + r"\\textsc{" + r"\2" + "}" + r"\3", text.encode("utf8")).decode("utf8")

def format_pinyin(text):
    """Replace '@xxx' by '\\textcolor{gray}{xxx}' in 'lx', 'dv', 'xv' fields (already in API).
    """
    import re
    return re.sub(r"(\w*)@(\w*)", r"\1" + r"\\textcolor{gray}{" + r"\2" + "}", text)

def format_uid(lexical_entry, font):
    """! @brief Transform unique identifier of a lexical entry in ASCII format.
    @param lexical_entry The targeted Lexical Entry LMF instance.
    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.
    @return A string representing the unique identifier in LaTeX format.
    """
    return unicode(lexical_entry.get_id())#.encode('ascii', 'ignore')

def format_link(lexical_entry, font):
    """! @brief Display hyperlink to a lexical entry in LaTeX format.
    @param lexical_entry The targeted Lexical Entry LMF instance.
    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.
    @return A string representing the hyperlink in LaTeX format.
    """
    result = "\\hyperlink{" + format_uid(lexical_entry, font) + "}{" + font[VERNACULAR](lexical_entry.get_lexeme())
    if lexical_entry.get_homonymNumber() is not None:
        result += " \\textsubscript{" + str(lexical_entry.get_homonymNumber()) + "}"
    result += "}"
    return result

def format_lexeme(lexical_entry, font):
    """! @brief 'lx', 'hm' and 'lc' fields are flipped if 'lc' field has data.
    @param lexical_entry The current Lexical Entry LMF instance.
    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.
    @return A string representing lexeme in LaTeX format.
    """
    lexeme = font[VERNACULAR](lexical_entry.get_lexeme())
    result = "\\vspace{1cm} \\hspace{-1cm} "
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
        result += lexeme
    result += " \\hspace{0.1cm} \\hypertarget{" + format_uid(lexical_entry, font) + "}{}" + EOL
    return result

def format_audio(lexical_entry, font):
    """! @brief Embed sound file into PDF.
    @param lexical_entry The current Lexical Entry LMF instance.
    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.
    @return A string embedding sound in LaTeX format.
    """
    from os.path import basename, isfile
    result = ""
    for form_representation in lexical_entry.get_form_representations():
        if form_representation.get_audio() is not None:
            # Embed local sound file
            # \includemedia[<options>]{<poster text>}{<main Flash (SWF) file or URL  |  3D (PRC, U3D) file>}
            # To include audio file in PDF, replace WAV extension by MP3 extension
            file_name = basename(form_representation.get_audio().get_fileName().replace(".wav", ".mp3"))
            if not isfile(form_representation.get_audio().get_fileName().replace(".wav", ".mp3").replace("file://", '')):
                print unicode(Warning("Sound file '%s' encountered for lexeme '%s' does not exist" % (file_name, lexical_entry.get_lexeme())))
                return result
            file_name = file_name.replace('_', '\string_').replace('-', '\string-')
            result += "\includemedia[\n" \
                "\taddresource=" + file_name + ",\n" \
                "\tflashvars={\n" \
                    "\t\tsource=" + file_name + "\n" \
                    "\t\t&autoPlay=true\n" \
                    "\t\t&autoRewind=true\n" \
                    "\t\t&loop=false\n" \
                    "\t\t&hideBar=true\n" \
                    "\t\t&volume=1.0\n" \
                    "\t\t&balance=0.0\n" \
                "}]{\includegraphics[scale=0.5]{sound1\string_bleu.jpg}}{APlayer.swf}"
            # \mediabutton[<options>]{<normal button text or graphic>}
            result += " \\hspace{0.1cm}\n"
    return result

def format_part_of_speech(lexical_entry, font):
    """! @brief Display part of speech in LaTeX format.
    @param lexical_entry The current Lexical Entry LMF instance.
    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.
    @return A string representing part of speech in LaTeX format.
    """
    result = ""
    if lexical_entry.get_partOfSpeech() is not None:
        result += "\\textcolor{teal}{\\textsc{" + lexical_entry.get_partOfSpeech() + "}}. "
    return result

def format_definitions(lexical_entry, font):
    """! @brief Glosses are supplanted by definitions.
    @param lexical_entry The current Lexical Entry LMF instance.
    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.
    @return A string representing glosses and definitions in LaTeX format.
    """
    result = ""
    for sense in lexical_entry.get_senses():
        for language in [VERNACULAR, ENGLISH, NATIONAL, REGIONAL]:
            if len(sense.find_definitions(language)) != 0:
                for definition in sense.find_definitions(language):
                    if language == VERNACULAR:
                        result += font[VERNACULAR](definition) + ". "
                    elif language == NATIONAL:
                        result += font[NATIONAL](definition) + ". "
                    elif language == REGIONAL:
                        result += "\\textit{[Regnl: " + font[REGIONAL](definition) + "]}. "
                    else:
                        result += definition + ". "
            elif len(sense.find_glosses(language)) != 0:
                for gloss in sense.find_glosses(language):
                    if language == VERNACULAR:
                        result += font[VERNACULAR](gloss) + ". "
                    elif language == NATIONAL:
                        result += font[NATIONAL](gloss) + ". "
                    elif language == REGIONAL:
                        result += "\\textit{[Regnl: " + font[REGIONAL](gloss) + "]}. "
                    else:
                        result += gloss + ". "
            if len(sense.get_translations(language)) != 0:
                for translation in sense.get_translations(language):
                    if language == NATIONAL:
                        result += font[NATIONAL](translation) + ". "
                    elif language == REGIONAL:
                        result += "\\textbf{rr:}\\textit{[Regnl: " + translation + "]}. "
                    else:
                        result += translation + ". "
    return result

def format_lt(lexical_entry, font):
    """! @brief Display 'lt' in LaTeX format.
    @param lexical_entry The current Lexical Entry LMF instance.
    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.
    @return A string representing 'lt' in LaTeX format.
    """
    # return "\\textit{Lit:} " + u"\u2018" + lexical_entry.get_lt() + u"\u2019" + ". "
    return ""

def format_sc(lexical_entry, font):
    """! @brief Display 'sc' in LaTeX format.
    @param lexical_entry The current Lexical Entry LMF instance.
    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.
    @return A string representing 'sc' in LaTeX format.
    """
    # return "\\textit{\uline{" + lexical_entry.get_sc() + "}}. "
    return ""

def format_rf(lexical_entry, font):
    """! @brief Display 'rf' in LaTeX format.
    @param lexical_entry The current Lexical Entry LMF instance.
    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.
    @return A string representing 'rf' in LaTeX format.
    """
    # return "\\textit{Ref:} " + lexical_entry.get_rf() + " "
    return ""

def format_examples(lexical_entry, font):
    """! @brief Display examples in LaTeX format.
    @param lexical_entry The current Lexical Entry LMF instance.
    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.
    @return A string representing examples in LaTeX format.
    """
    result = ""
    for sense in lexical_entry.get_senses():
        for context in sense.get_contexts():
            result += "\\begin{exe}\n"
            for example in context.find_written_forms(VERNACULAR):
                result += "\\sn " + font[VERNACULAR](example) + "\n"
            for example in context.find_written_forms(ENGLISH):
                result += "\\trans " + example + "\n"
            for example in context.find_written_forms(NATIONAL):
                result += "\\trans \\textit{" + font[NATIONAL](example) + "}\n"
            for example in context.find_written_forms(REGIONAL):
                result += "\\trans \\textit{[" + font[REGIONAL](example) + "]}\n"
            result += "\\end{exe}\n"
    return result

def format_usage_notes(lexical_entry, font):
    """! @brief Display usage notes in LaTeX format.
    @param lexical_entry The current Lexical Entry LMF instance.
    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.
    @return A string representing usage notes in LaTeX format.
    """
    result = ""
    for sense in lexical_entry.get_senses():
        for usage in sense.find_usage_notes(language=VERNACULAR):
            result += "\\textit{VerUsage:} " + font[VERNACULAR](usage) + " "
        for usage in sense.find_usage_notes(language=ENGLISH):
            result += "\\textit{Usage:} " + usage + " "
        for usage in sense.find_usage_notes(language=NATIONAL):
            result += "\\textit{" + font[NATIONAL](usage) + "} "
        for usage in sense.find_usage_notes(language=REGIONAL):
            result += "\\textit{[" + font[REGIONAL](usage) + "]} "
    return result

def format_encyclopedic_informations(lexical_entry, font):
    """! @brief Display encyclopedic informations in LaTeX format.
    @param lexical_entry The current Lexical Entry LMF instance.
    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.
    @return A string representing encyclopedic informations in LaTeX format.
    """
    result = ""
    for sense in lexical_entry.get_senses():
        for information in sense.find_encyclopedic_informations(language=VERNACULAR):
            result += font[VERNACULAR](information) + " "
        for information in sense.find_encyclopedic_informations(language=ENGLISH):
            result += information + " "
        for information in sense.find_encyclopedic_informations(language=NATIONAL):
            result += font[NATIONAL](information) + " "
        for information in sense.find_encyclopedic_informations(language=REGIONAL):
            result += "\\textit{[" + font[REGIONAL](information) + "]} "
    return result

def format_restrictions(lexical_entry, font):
    """! @brief Display restrictions in LaTeX format.
    @param lexical_entry The current Lexical Entry LMF instance.
    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.
    @return A string representing restrictions in LaTeX format.
    """
    result = ""
    for sense in lexical_entry.get_senses():
        for restriction in sense.find_restrictions(language=VERNACULAR):
            result += "\\textit{VerRestrict:} " + font[VERNACULAR](restriction) + " "
        for restriction in sense.find_restrictions(language=ENGLISH):
            result += "\\textit{Restrict:} " + restriction + " "
        for restriction in sense.find_restrictions(language=NATIONAL):
            result += "\\textit{" + font[NATIONAL](restriction) + "} "
        for restriction in sense.find_restrictions(language=REGIONAL):
            result += "\\textit{[" + font[REGIONAL](restriction) + "]} "
    return result

def format_lexical_functions(lexical_entry, font):
    """! @brief Display lexical functions in LaTeX format.
    @param lexical_entry The current Lexical Entry LMF instance.
    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.
    @return A string representing lexical functions in LaTeX format.
    """
    result = ""
    # result += "\\textit{" + lexical_entry.get_lf() + ": }"
    # result += lexical_entry.get_le() + " "
    # result += lexical_entry.get_ln() + " "
    # result += lexical_entry.get_lr() + " "
    return result

def format_related_forms(lexical_entry, font):
    """! @brief Display related forms in LaTeX format.
    @param lexical_entry The current Lexical Entry LMF instance.
    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.
    @return A string representing related forms in LaTeX format.
    """
    result = ""
    for related_form in lexical_entry.get_related_forms(mdf_semanticRelation["sy"]):
        result += "\\textit{Syn:} "
        if related_form.get_lexical_entry() is not None:
            result += format_link(related_form.get_lexical_entry(), font)
        else:
            result += font[VERNACULAR](related_form.get_lexeme())
        result += ". "
    for related_form in lexical_entry.get_related_forms(mdf_semanticRelation["an"]):
        result += "\\textit{Ant:} "
        if related_form.get_lexical_entry() is not None:
            result += format_link(related_form.get_lexical_entry(), font)
        else:
            result += font[VERNACULAR](related_form.get_lexeme())
        result += ". "
    for morphology in lexical_entry.get_morphologies():
        result += "\\textit{Morph:} " + font[VERNACULAR](morphology) + ". "
    for related_form in lexical_entry.get_related_forms(mdf_semanticRelation["cf"]):
        result += "\\textit{See:} "
        if related_form.get_lexical_entry() is not None:
            result += format_link(related_form.get_lexical_entry(), font)
        else:
            result += font[VERNACULAR](related_form.get_lexeme())
        result += " "
    # ce
    # cn
    # cr
    # result += "\\textit{See main entry:} " + font[VERNACULAR](lexical_entry.get_mn()) + ". "
    return result

def format_variant_forms(lexical_entry, font):
    """! @brief Display variant forms in LaTeX format.
    @param lexical_entry The current Lexical Entry LMF instance.
    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.
    @return A string representing variant forms in LaTeX format.
    """
    result = ""
    for form_representation in lexical_entry.get_form_representations():
        if form_representation.get_variantForm() is not None:
            result += "\\textit{Variant:} " + font[VERNACULAR](form_representation.get_variantForm()) + " "
        if form_representation.get_comment(ENGLISH) is not None:
            result +=  "(" + form_representation.get_comment(ENGLISH) + ") "
        if form_representation.get_comment(NATIONAL) is not None:
            result +=  "(" + font[NATIONAL](form_representation.get_comment(NATIONAL)) + ") "
        if form_representation.get_comment(REGIONAL) is not None:
            result +=  "(" + font[REGIONAL](form_representation.get_comment(REGIONAL)) + ") "
    return result

def format_borrowed_word(lexical_entry, font):
    """! @brief Display borrowed word in LaTeX format.
    @param lexical_entry The current Lexical Entry LMF instance.
    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.
    @return A string representing borrowed word in LaTeX format.
    """
    result = ""
    if lexical_entry.get_borrowed_word() is not None:
        result += "\\textit{From:} " + lexical_entry.get_borrowed_word()
        if lexical_entry.get_written_form() is not None:
            result += " " + lexical_entry.get_written_form()
        result += ". "
    return result

def format_etymology(lexical_entry, font):
    """! @brief Display etymology in LaTeX format.
    @param lexical_entry The current Lexical Entry LMF instance.
    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.
    @return A string representing etymology in LaTeX format.
    """
    result = ""
    if lexical_entry.get_etymology() is not None:
        result += "\\textit{Etym:} \\textbf{" + lexical_entry.get_etymology() + "} "
    if lexical_entry.get_etymology_gloss() is not None:
        result += u"\u2018" + lexical_entry.get_etymology_gloss() + u"\u2019" + ". "
    return result

def format_paradigms(lexical_entry, font):
    """! @brief Display all paradigms in LaTeX format.
    @param lexical_entry The current Lexical Entry LMF instance.
    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.
    @return A string representing all paradigms in LaTeX format.
    """
    result = ""
    for paradigm in lexical_entry.find_paradigms():
        result += "\\textit{Prdm:} \\textbf{" + paradigm + "}. "
    for paradigm in lexical_entry.find_paradigms(grammatical_number=pd_grammaticalNumber["sg"]):
        result += "\\textit{Sg:} \\textbf{" + paradigm + "} "
    for paradigm in lexical_entry.find_paradigms(grammatical_number=pd_grammaticalNumber["pl"]):
        result += "\\textit{Pl:} \\textbf{" + paradigm + "} "
    # result += "\\textit{Redup:} \\textbf{" + lexical_entry.get_rd() + "} "
    for paradigm in lexical_entry.find_paradigms(person=pd_person[1], grammatical_number=pd_grammaticalNumber['s']):
        result += "\\textit{1s:} \\textbf{" + paradigm + "} "
    for paradigm in lexical_entry.find_paradigms(person=pd_person[2], grammatical_number=pd_grammaticalNumber['s']):
        result += "\\textit{2s:} \\textbf{" + paradigm + "} "
    for paradigm in lexical_entry.find_paradigms(person=pd_person[3], grammatical_number=pd_grammaticalNumber['s']):
        result += "\\textit{3s:} \\textbf{" + paradigm + "} "
    for paradigm in lexical_entry.find_paradigms(anymacy=pd_anymacy[4], grammatical_number=pd_grammaticalNumber['s']):
        result += "\\textit{3sn:} \\textbf{" + paradigm + "} "
    for paradigm in lexical_entry.find_paradigms(person=pd_person[1], grammatical_number=pd_grammaticalNumber['d']):
        result += "\\textit{1d:} \\textbf{" + paradigm + "} "
    for paradigm in lexical_entry.find_paradigms(person=pd_person[2], grammatical_number=pd_grammaticalNumber['d']):
        result += "\\textit{2d:} \\textbf{" + paradigm + "} "
    for paradigm in lexical_entry.find_paradigms(person=pd_person[3], grammatical_number=pd_grammaticalNumber['d']):
        result += "\\textit{3d:} \\textbf{" + paradigm + "} "
    for paradigm in lexical_entry.find_paradigms(anymacy=pd_anymacy[4], grammatical_number=pd_grammaticalNumber['d']):
        result += "\\textit{3dn:} \\textbf{" + paradigm + "} "
    for paradigm in lexical_entry.find_paradigms(person=pd_person[1], grammatical_number=pd_grammaticalNumber['p']):
        result += "\\textit{1p:} \\textbf{" + paradigm + "} "
    for paradigm in lexical_entry.find_paradigms(person=pd_person[1], grammatical_number=pd_grammaticalNumber['p'], clusivity=pd_clusivity['e']):
        result += "\\textit{1px:} \\textbf{" + paradigm + "} "
    for paradigm in lexical_entry.find_paradigms(person=pd_person[1], grammatical_number=pd_grammaticalNumber['p'], clusivity=pd_clusivity['i']):
        result += "\\textit{1pi:} \\textbf{" + paradigm + "} "
    for paradigm in lexical_entry.find_paradigms(person=pd_person[2], grammatical_number=pd_grammaticalNumber['p']):
        result += "\\textit{2p:} \\textbf{" + paradigm + "} "
    for paradigm in lexical_entry.find_paradigms(person=pd_person[3], grammatical_number=pd_grammaticalNumber['p']):
        result += "\\textit{3p:} \\textbf{" + paradigm + "} "
    for paradigm in lexical_entry.find_paradigms(anymacy=pd_anymacy[4], grammatical_number=pd_grammaticalNumber['p']):
        result += "\\textit{3pn:} \\textbf{" + paradigm + "} "
    return result

def format_table(lexical_entry, font):
    """! @brief Display a table in LaTeX format.
    @param lexical_entry The current Lexical Entry LMF instance.
    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.
    @return A string representing a table in LaTeX format.
    """
    return ""

def format_semantic_domains(lexical_entry, font):
    """! @brief Display semantic domains in LaTeX format.
    @param lexical_entry The current Lexical Entry LMF instance.
    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.
    @return A string representing semantic domains in LaTeX format.
    """
    result = ""
    for semantic_domain in lexical_entry.get_semantic_domains():
        result += "\\textit{SD:} " + semantic_domain + ". "
    # is
    # result += "\\textit{Semantics:} " + lexical_entry.get_is() + ". "
    # th
    # result += "\\textit{Thes:} " + lexical_entry.get_th() + ". "
    return result

def format_bibliography(lexical_entry, font):
    """! @brief Display bibliography in LaTeX format.
    @param lexical_entry The current Lexical Entry LMF instance.
    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.
    @return A string representing bibliography in LaTeX format.
    """
    result = ""
    if lexical_entry.get_bibliography() is not None:
        result += "\\textit{Read:} " + lexical_entry.get_bibliography() + ". "
    return result

def format_picture(lexical_entry, font):
    """! @brief Display a picture in LaTeX format.
    @param lexical_entry The current Lexical Entry LMF instance.
    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.
    @return A string representing a picture in LaTeX format.
    """
    # return "(" + lexical_entry.get_pc() + ") "
    return ""

def format_notes(lexical_entry, font):
    """! @brief Display all notes in LaTeX format.
    @param lexical_entry The current Lexical Entry LMF instance.
    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.
    @return A string representing all notes in LaTeX format.
    """
    result = ""
    for note in lexical_entry.find_notes(type="general"):
        result += "\\textit{[Note: " + note + "]} "
    for note in lexical_entry.find_notes(type="phonology"):
        result += "\\textit{[Phon: " + note + "]} "
    for note in lexical_entry.find_notes(type="grammar"):
        result += "\\textit{[Gram: " + note + "]} "
    for note in lexical_entry.find_notes(type="discourse"):
        result += "\\textit{[Disc: " + note + "]} "
    for note in lexical_entry.find_notes(type="anthropology"):
        result += "\\textit{[Ant: " + note + "]} "
    for note in lexical_entry.find_notes(type="sociolinguistics"):
        result += "\\textit{[Socio: " + note + "]} "
    for note in lexical_entry.find_notes(type="question"):
        result += "\\textit{[Ques: " + note + "]} "
    return result

def format_source(lexical_entry, font):
    """! @brief Display source in LaTeX format.
    @param lexical_entry The current Lexical Entry LMF instance.
    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.
    @return A string representing source in LaTeX format.
    """
    # return "\\textit{Source:} " + lexical_entry.get_so() + ". "
    return ""

def format_status(lexical_entry, font):
    """! @brief Display status in LaTeX format.
    @param lexical_entry The current Lexical Entry LMF instance.
    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.
    @return A string representing status in LaTeX format.
    """
    result = ""
    if lexical_entry.get_status() is not None:
        result += "\\textit{Status:} " + lexical_entry.get_status()
    return result

def format_date(lexical_entry, font):
    """! @brief Do not display date in LaTeX format.
    @param lexical_entry The current Lexical Entry LMF instance.
    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.
    @return An empty string.
    """
    return ""
