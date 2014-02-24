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
        hdr = self.open_read("dev/scripts/test/japhug/expected_result/header.tex")
        header = hdr.readlines()
        hdr.close()
        return header

    def write_fields(self):
        """Write LaTeX output file.
        """
        tex_file = self.open_write(self.options.output)
        tree = parse(self.options.input)
        root = tree.getroot()
        # Number of 'lx'
        sec_nb = 0
        for element in root.iter():
            if element.tag == "lx":
                sec_nb += 1
                tex_file.write("\n\label{sec:" + str(sec_nb) + "}\n")
                tex_file.write("\section*{\ipa{" + element.text + "}}\n")
            elif element.tag == "se":
                tex_file.write("\subsection*{\ipa{" + element.text + "}}\n")
            elif element.tag == "ps":
                tex_file.write("\\textit{" + element.text + "}\n")
            elif element.tag == "a":
                tex_file.write("\ipa{" + element.text + "}\n")
            elif element.tag == "mr":
                tex_file.write("\ipa{" + element.text + "}\n")
            elif element.tag == "ge":
                tex_file.write(element.text + "\n")
            elif element.tag == "gn":
                tex_file.write("\zh{" + element.text + "}\n")
            elif element.tag == "xv":
                tex_file.write("\ipa{" + element.text + "}\n")
            elif element.tag == "xn":
                tex_file.write("\zh{" + element.text + "}\n")
            elif element.tag == "xe":
                tex_file.write(element.text + "\n")
            elif element.tag == "et":
                tex_file.write("\ipa{" + element.text + "}\n")
            elif element.tag == "un":
                tex_file.write("\zh{" + element.text + "}\n")
            elif element.tag == "uv":
                tex_file.write("\ipa{" + element.text + "}\n")
            elif element.tag == "dv":
                tex_file.write("\ipa{" + element.text + "}\n")
            elif element.tag == "dn":
                tex_file.write("\zh{" + element.text + "}\n")
            elif element.tag == "de":
                tex_file.write(element.text + "\n")
            elif element.tag == "nq":
                tex_file.write("QUESTION: \ipa{" + element.text + "}\n")
            elif element.tag == "cf" or element.tag == "sy" or element.tag == "an":
                tex_file.write("\\ref{sec:0} -> " + element.text + "\n")
            elif element.tag == "wav" or element.tag == "wav8" or element.tag == "hbf" or element.tag == "ng" or element.tag == "dt":
                # Remove
                pass
            elif element.tag.find("Group") != -1 :
                # Remove
                pass
            elif element.tag == "toolbox_data" or element.tag == "header" or element.tag == "_sh" :
                # Remove
                pass
            else:
                tex_file.write(element.tag + " " + element.text + " ERR\n")
        tex_file.close()
        print sec_nb, "record(s)"

    def main(self):
        self.parse_options()
        # Convert to LaTeX
        self.write_fields()

if __name__ == '__main__':
    converter = Xml2Tex()
    converter.main()
    # Exit program properly
    sys.exit(0)
