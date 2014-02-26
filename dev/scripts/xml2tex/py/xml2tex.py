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
        # Tags added by Toolbox
        tags_tb = set(["toolbox_data", "header", "_sh"])
        # Tags that need additional references
        tags_ref = set(["sy", "an", "cf"])
        # japhug : 'ipa' = API ; chinois : 'zh' ; tibetain : r
        format = dict({
            "lx"    : lambda e: "\n\\vspace{1cm} \\hspace{-1cm} {\Large \ipa{" + e.text + "}} \\hspace{0.2cm} \\hypertarget{" + e.attrib['id'] + "}{}\n",
            "wav"   : lambda e: "",
            "wav8"  : lambda e: "",
            "hbf"   : lambda e: "",
            "dt"    : lambda e: "",
            "se"    : lambda e: "\n\\hspace{0.2cm} {\large \ipa{" + e.text + "}}\n",
            "et"    : lambda e: "\\textit{Etym:} \\textbf{\ipa{" + e.text + "}}.\n",
            "ps"    : lambda e: "\\textcolor{cyan}{\\textit{" + e.text + "}}\n",
            "sy"    : lambda e: "\\textit{Syn:} ",
            "an"    : lambda e: "\\textit{Ant:} ",
            "cf"    : lambda e: "\\textit{See:} ",
            "ng"    : lambda e: "",
            "nq"    : lambda e: "\\textit{[Ques:} \ipa{" + e.text + "} \\textit{]}.\n",
            "a"     : lambda e: "\\textit{Variant:} \\textbf{\ipa{" + e.text + "}}.\n",
            "mr"    : lambda e: "\\textit{Morph:} \\textbf{\ipa{" + e.text + "}}.\n",
            "ms"    : lambda e: "\\textit{Morph:} \\textbf{\ipa{" + e.text + "}}.\n",
            "a2s"   : lambda e: "\\textit{[Theme du passe:} \ipa{" + e.text + "} \\textit{]}.\n",
            "comit" : lambda e: "\\textit{[Comitatif:} \ipa{" + e.text + "} \\textit{]}.\n",
            "constr": lambda e: "\\textit{[Construction:} \ipa{" + e.text + "} \\textit{]}.\n",
            "dv"    : lambda e: "\\textbf{\ipa{" + e.text + "}}.\n",
            "de"    : lambda e: e.text + ".\n",
            "ge"    : lambda e: e.text + "\n",
            "dn"    : lambda e: "\\textit{\zh{" + e.text + "}}\n",
            "gn"    : lambda e: "\\textit{\zh{" + e.text + "}}\n",
            "gr"    : lambda e: "",
            "uv"    : lambda e: "\\textit{Usage:} \\textbf{\ipa{" + e.text + "}}.\n",
            "un"    : lambda e: "\\textit{\zh{" + e.text + "}}\n",
            "ev"    : lambda e: "\\textbf{\ipa{" + e.text + "}}.\n",
            "en"    : lambda e: "\\textit{\zh{" + e.text + "}}\n",
            "er"    : lambda e: "",
            "xv"    : lambda e: "\\hspace{0.1cm} \\textbullet \\hspace{0.1cm} \\textcolor{blue}{\ipa{" + e.text + "}} - \n",
            "xe"    : lambda e: e.text + "\n",
            "xn"    : lambda e: "\\textit{\zh{" + e.text + "}}\n",
            "xr"    : lambda e: ""
        })
        # Keep reference errors
        errors = set()
        for element in self.tree.getroot().iter():
            if element.text.find("{") != -1:
                element.text = self.format_font(element.text)
            if element.text == '_':
                # LaTeX returns error in case of "\ipa{_}"
                pass
            elif element.tag in tags_tb:
                # Remove
                pass
            elif element.tag.find("Group") != -1 :
                # Remove
                pass
            else:
                tex_file.write(format[element.tag](element))
                if element.tag in tags_ref:
                    found = False
                    for lx in self.tree.iterfind("lxGroup/lx"):
                        if lx.text == element.text:
                            tex_file.write("\\hyperlink{" + lx.get('id') + "}{" + lx.text + "}.\n")
                            found = True
                            break
                    if not found:
                        # Just write the reference without hyperlink and log error
                        tex_file.write(element.text + ".\n")
                        errors.add(element.text)
        for error in errors:
            print error
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
