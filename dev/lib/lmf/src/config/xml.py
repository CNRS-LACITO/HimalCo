#! /usr/bin/env python

"""! @package config
"""

from core.lexical_resource import LexicalResource
from core.lexicon import Lexicon
from utils.xml_format import parse_xml
from utils.error_handling import InputError

# If an LMF module needs to access languages or fonts, copy following lines:
# import config
# print config.xml.vernacular, config.xml.English, config.xml.national, config.xml.regional, config.xml.French
# print config.xml.font

def sort_order_read(filename):
    """! @brief Read an XML file giving sort order.
    @param filename The name of the XML file to read with full path, for instance 'user/default/sort_order.xml'.
    @return A Python dictionary of ordered characters.
    """
    order = dict()
    root = parse_xml(filename)
    # Parse XML elements
    for rules in root:
        # XML elements "rules" have 1 XML attribute: "level"
        if rules.tag != "rules":
            raise InputError(module_name + ".py", "XML file '%s' is not well-formatted." % filename)
        for rule in rules:
            # XML elements "rule" have 2 XML attributes: one for the character ("str"), a second for the rank value ("rank")
            if rule.tag != "rule":
                raise InputError(module_name + ".py", "XML file '%s' is not well-formatted." % filename)
            order.update({rule.attrib["str"] : float(rule.attrib["rank"])})
    return order

def config_read(filename):
    """! @brief Read an XML file giving the user configuration.
    @param filename The name of the XML file to read with full path, for instance 'user/default/config.xml'.
    @return A Lexical Resource.
    """
    import config.xml
    configuration = parse_xml(filename)
    # Parse XML elements
    for format in configuration:
        if format.tag == "Language":
            # XML element "Language" have several XML subelements "lang"
            for lang in format:
                # XML elements "lang" have 2 XML attributes: one for the nature of the language ("att"), a second for the language code ("val")
                exec("config.xml." + lang.attrib["att"] + " = '" + lang.attrib["val"] + "'")
        elif format.tag == "Font":
            config.xml.font = dict()
            # XML element "Font" have several XML subelements "font"
            for font in format:
                # XML elements "font" have 2 XML attributes: one for the nature of the language ("att"), a second for the variable name ("var")
                exec("l = lambda " + font.attrib['var'] + ": " + font.text)
                config.xml.font.update({font.attrib['att']: l})
        elif format.tag == "LMF":
            # Create lexical resource and set DTD version
            lexical_resource = LexicalResource(format[0].attrib["dtdVersion"])
            for object in format[0]:
                if object.tag == "GlobalInformation":
                    # Set global information
                    for feat in object:
                        if feat.attrib["att"] == "languageCode":
                            lexical_resource.set_language_code(feat.attrib["val"])
                        elif feat.attrib["att"] == "author":
                            lexical_resource.set_author(feat.attrib["val"])
                        elif feat.attrib["att"] == "version":
                            lexical_resource.set_version(feat.attrib["val"])
                        elif feat.attrib["att"] == "lastUpdate":
                            lexical_resource.set_last_update(feat.attrib["val"])
                        elif feat.attrib["att"] == "license":
                            lexical_resource.set_license(feat.attrib["val"])
                        elif feat.attrib["att"] == "characterEncoding":
                            lexical_resource.set_character_encoding(feat.attrib["val"])
                        elif feat.attrib["att"] == "dateCoding":
                            lexical_resource.set_date_coding(feat.attrib["val"])
                        elif feat.attrib["att"] == "creationDate":
                            lexical_resource.set_creation_date(feat.attrib["val"])
                        elif feat.attrib["att"] == "projectName":
                            lexical_resource.set_project_name(feat.attrib["val"])
                        elif feat.attrib["att"] == "description":
                            lexical_resource.set_description(feat.attrib["val"])
                elif object.tag == "Lexicon":
                    # Create lexicon and set identifier
                    lexicon = Lexicon(object.attrib["id"])
                    # Set lexicon attributes
                    for feat in object:
                        if feat.attrib["att"] == "language":
                            lexicon.set_language(feat.attrib["val"])
                        elif feat.attrib["att"] == "languageScript":
                            lexicon.set_languageScript(feat.attrib["val"])
                        elif feat.attrib["att"] == "label":
                            lexicon.set_label(feat.attrib["val"])
                        elif feat.attrib["att"] == "lexiconType":
                            lexicon.set_lexiconType(feat.attrib["val"])
                        elif feat.attrib["att"] == "entrySource":
                            lexicon.set_entrySource(feat.attrib["val"])
                        elif feat.attrib["att"] == "localPath":
                            lexicon.set_localPath(feat.attrib["val"])
                    # Attach lexicon to the lexical resource
                    lexical_resource.add_lexicon(lexicon)
        elif format.tag == "MDF":
            pass
        elif format.tag == "LaTeX":
            pass
        else:
            raise InputError(module_name + ".py", "XML file '%s' is not well-formatted." % filename)
    return lexical_resource
