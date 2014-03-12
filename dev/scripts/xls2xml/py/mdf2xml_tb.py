#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Go under dev/scripts/ and launch this script using the following command:
# python xls2xml/py/mdf2xml_tb.py

# Import system Python module
import sys
# Import utilities
sys.path.append(".")
from common import *

# Default values of command line arguments
DEFAULT_INPUT = DICT_NA
DEFAULT_OUTPUT = None
DEFAULT_GRAMMAR = GRAMMAR_NA
DEFAULT_TEST = None

# XmlFormat inherits from InOut
class Mdf2Xml(MdfFormat, XmlFormat):
    def __init__(self):
        MdfFormat.__init__(self)

    def parse_options(self):
        """Get command line arguments.
        """
        # Options management
        from optparse import OptionParser
        parser = OptionParser()
        parser.add_option("-v", "--verbose", dest="verbose", action="store_true", default=False, help="print more details to stdout [default=False]")
        parser.add_option("-i", "--input", dest="input", action="store", default=DEFAULT_INPUT, help="input text file [default=" + str(DEFAULT_INPUT) + "]")
        parser.add_option("-o", "--output", dest="output", action="store", default=DEFAULT_OUTPUT, help="output xml file [default=" + str(DEFAULT_OUTPUT) + "]")
        parser.add_option("-g", "--grammar", dest="grammar", action="store", default=DEFAULT_GRAMMAR, help="grammar to use [default=" + str(DEFAULT_GRAMMAR) + "]")
        parser.add_option("-t", "--test", dest="test", action="store", default=DEFAULT_TEST, help="test to run [default=" + str(DEFAULT_TEST) + "]")
        self.options = parser.parse_args()[0]
        # Tests
        if self.options.test is not None:
            if self.options.test == "na1":
                self.options.input = "obj/na1.mdf"
            elif self.options.test == "na":
                self.options.output = "obj/Dictionary_na.xml"
            else:
                sys.exit(-1)
        # Compute output filename
        if self.options.output is None:
            self.options.output = "./obj/" + self.options.input[self.options.input.rfind('/') + 1:self.options.input.rfind('.') + 1] + "xml"

    def main(self):
        self.create_obj()
        self.parse_options()
        self.process_data()
        self.write_result()
        self.display_result()

if __name__ == '__main__':
    converter = Mdf2Xml()
    converter.main()
    # Exit program properly
    sys.exit(0)
