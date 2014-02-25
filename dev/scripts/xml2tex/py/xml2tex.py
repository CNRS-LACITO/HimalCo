#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Go under dev/scripts/ and launch this script using the following command:
# python xml2tex/py/xml2tex.py

# Import system Python module
import sys
# Import utilities
sys.path.append(".")
from common import *

# Default values of command line arguments
DEFAULT_INPUT = None
DEFAULT_OUTPUT = None
DEFAULT_TEST = None

class Xml2Tex(InOut, XmlFormat):
    def __init__(self):
        XmlFormat.__init__(self)

    def parse_options(self):
        """Get command line arguments.
        """
        # Options management
        from optparse import OptionParser
        parser = OptionParser()
        parser.add_option("-v", "--verbose", dest="verbose", action="store_true", default=False, help="print more details to stdout [default=False]")
        parser.add_option("-i", "--input", dest="input", action="store", default=DEFAULT_INPUT, help="input XML file [default=" + str(DEFAULT_INPUT) + "]")
        parser.add_option("-o", "--output", dest="output", action="store", default=DEFAULT_OUTPUT, help="output LaTeX file [default=" + str(DEFAULT_OUTPUT) + "]")
        parser.add_option("-t", "--test", dest="test", action="store", default=DEFAULT_TEST, help="test to run [default=" + str(DEFAULT_TEST) + "]")
        self.options = parser.parse_args()[0]
        # Tests
        if self.options.test is not None:
            if self.options.test == "japhug":
                self.options.input = "obj/Dictionary.xml"
            else:
                sys.exit(-1)
        # Compute output filename
        if self.options.output is None:
            self.options.output = "./obj/" + self.options.input[self.options.input.rfind('/') + 1:self.options.input.rfind('.') + 1] + "tex"

    def compute_header(self):
        """Create LaTeX header.
        """
        hdr = self.open_read("./test/japhug/expected_result/header.tex")
        header = hdr.read()
        hdr.close()
        return header

    def add_lx_id(self):
        """Add 'lx' identifiers.
        """
        self.tree = parse(self.options.input)
        id = 0
        for element in self.tree.getroot().iter():
            if element.tag == "lx":
                id += 1
                element.attrib['id'] = str(id)
        self.tree.write(self.options.input.rstrip(".xml") + "_new.xml", encoding=CODEC)
        print id, "record(s)"

    def format_font(self, text):
        """Replace '{xxx}' or '\{xxx}' by '\ipa{xxx}'.
        """
        return text.replace('\\', '').replace('{', "\\ipa{")

    def write_fields(self):
        """Write LaTeX output file.
        """
        tex_file = self.open_write(self.options.output)
        tex_file.write(self.compute_header())
        tex_file.write("\n\\begin{document}\n")
        tex_file.write("\\begin{multicols}{2}\n")
        tags_tb = set(["toolbox_data", "header", "_sh"])
        tags_to_ignore = set(["wav", "wav8", "hbf", "dt", "ng", "gr", "er", "xr"]) # r -> tibetain
        tags_none = set(["de", "ge", "xe"])
        tags_ipa = set(["et", "a", "mr", "dv", "uv", "ev", "xv"]) # API
        tags_zh = set(["dn", "gn", "un", "en", "xn"])
        tags_ref = set(["sy", "an", "cf"])
        format = dict({"et":"\\textit{Etym:} ", "a":"\\textit{Variant:} ", "mr":"\\textit{Morph:} ", "dv":"", "uv":"\\textit{Usage:} ", "ev":"", "xv":"", "sy":"\\textit{Syn:} ", "an":"\\textit{Ant:} ", "cf":"\\textit{See:} "})
        for element in self.tree.getroot().iter():
            if element.text.find("{") != -1:
                element.text = self.format_font(element.text)
            # LaTeX returns error in case of "\ipa{_}"
            if element.text == '_':
                pass
            elif element.tag == "lx":
                tex_file.write("\n\section*{\ipa{" + element.text + "}}\n")
                #tex_file.write("\label{sec:" + element.attrib['id'] + "}\n")
                tex_file.write("\\hypertarget{" + element.attrib['id'] + "}{" + element.text + "}\n")
            elif element.tag == "se":
                tex_file.write("\subsection*{\ipa{" + element.text + "}}\n")
            elif element.tag == "ps":
                tex_file.write("\\textit{" + element.text + "}.\n")
            elif element.tag in tags_tb or element.tag in tags_to_ignore:
                # Remove
                pass
            elif element.tag in tags_none:
                tex_file.write(element.text + "\n")
            elif element.tag in tags_ipa:
                tex_file.write(format[element.tag])
                tex_file.write("\\bf{\ipa{" + element.text + "}}.\n")
            elif element.tag in tags_zh:
                tex_file.write("\\textit{\zh{" + element.text + "}}.\n")
            elif element.tag in tags_ref:
                tex_file.write(format[element.tag])
                for lx in self.tree.iterfind("lxGroup/lx"):
                    if lx.text == element.text:
                        #tex_file.write("\\ref{sec:" + lx.get('id') + "}\n")
                        tex_file.write("\\hyperlink{" + lx.get('id') + "}{" + lx.text + "}.\n")
                        break
            elif element.tag == "nq":
                tex_file.write("\\textit{[Ques:} \ipa{" + element.text + "}\\textit{]}\n")
            elif element.tag == "a2s":
                tex_file.write("THEME DU PASSE: \ipa{" + element.text + "}\n")
            elif element.tag == "comit":
                tex_file.write("COMITATIF: \ipa{" + element.text + "}\n")
            elif element.tag == "constr":
                tex_file.write("CONSTRUCTION: \ipa{" + element.text + "}\n")
            elif element.tag.find("Group") != -1 :
                # Remove
                pass
            else:
                print "ERR Unknown tag:", element.tag
                sys.exit(-1)
        tex_file.write("\end{multicols}\n")
        tex_file.write("\n\end{document}\n")
        tex_file.close()

    def main(self):
        self.parse_options()
        # Add 'lx' identifiers
        self.add_lx_id()
        # Convert to LaTeX
        self.write_fields()

if __name__ == '__main__':
    converter = Xml2Tex()
    converter.main()
    # Exit program properly
    sys.exit(0)
